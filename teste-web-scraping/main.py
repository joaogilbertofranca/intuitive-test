import requests
from bs4 import BeautifulSoup
import zipfile
import os

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def get_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for a_tag in soup.find_all('a', href=True):
        if "pdf" in a_tag['href'].lower():
            links.append(a_tag['href'])
    
    print("Links encontrados:", links)
    
    return links

def get_unique_filename(filename):
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(new_filename):
        new_filename = f"{base_name}_{counter}{extension}"
        counter += 1
    
    return new_filename

def download_pdfs(links):
    pdf_files = []
    
    for link in links:
        if not link.startswith("http"):
            link = "https://www.gov.br" + link  
        
        filename = link.split('/')[-1]
        
        unique_filename = get_unique_filename(filename)
        
        response = requests.get(link)
        
        if response.status_code == 200:
            with open(unique_filename, 'wb') as f:
                f.write(response.content)
            
            pdf_files.append(unique_filename)
            print(f"Downloaded: {unique_filename}")
        else:
            print(f"Falha ao baixar {link}")
    
    return pdf_files

def create_zip(pdf_files):
    zip_filename = "anexos.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in pdf_files:
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))
                os.remove(file)  
                print(f"Arquivo {file} adicionado ao ZIP e removido.")
            else:
                print(f"Arquivo {file} não encontrado para adicionar ao ZIP.")
    
    print(f"Todos os PDFs foram compactados em {zip_filename}")

def main():
    
    pdf_links = get_pdf_links(url)
    
    if not pdf_links:
        print("Nenhum link de PDF encontrado!")
        return
    
    pdf_files = download_pdfs(pdf_links)
    
    create_zip(pdf_files)

if __name__ == "__main__":
    main()
