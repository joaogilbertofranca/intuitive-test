import pdfplumber
import pandas as pd
import zipfile
import os

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = []
        
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                full_text.extend(table)  

        df = pd.DataFrame(full_text[1:], columns=full_text[0])  
        return df

def replace_abbreviations(df):
    replacements = {
        "OD": "Óptica Domiciliar",  
        "AMB": "Ambulatório"
    }

    df = df.replace(replacements)
    return df

def save_to_csv(df, output_csv):
    df.to_csv(output_csv, index=False, encoding="utf-8")

def create_zip(csv_filename, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))
    os.remove(csv_filename)  

def main():
    pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    
    df = extract_table_from_pdf(pdf_path)

    df = replace_abbreviations(df)

    csv_filename = "Rol_de_Procedimentos.csv"
    save_to_csv(df, csv_filename)

    zip_filename = "Teste_João_Gilberto.zip"  
    create_zip(csv_filename, zip_filename)

    print(f"Arquivo ZIP {zip_filename} criado com sucesso!")

if __name__ == "__main__":
    main()
