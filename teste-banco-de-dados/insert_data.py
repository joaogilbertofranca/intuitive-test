import csv
import os
from db import db
from tqdm import tqdm 

def convert_to_float(value):
    return float(value.replace(',', '.')) if value else None

def convert_to_int(value):
    return int(value) if value.isdigit() else None

def insert_demonstracoes_contabeis(csv_files):
    conn = db.get_connection()
    try:
        with conn.cursor() as cursor:
            for csv_file in csv_files:
              
                with open(csv_file, encoding='utf-8') as f:
                    total_lines = sum(1 for line in f) - 1 
                
                with open(csv_file, encoding='utf-8') as f:
                    reader = csv.reader(f, delimiter=';')
                    next(reader) 

                    for row in tqdm(reader, total=total_lines, desc=f"Inserindo {os.path.basename(csv_file)}"):
                        cursor.execute('''
                            INSERT INTO demonstracoes_contabeis (
                                data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
                            ) VALUES (%s, %s, %s, %s, %s, %s)
                        ''', (row[0], convert_to_int(row[1]), convert_to_int(row[2]), row[3], 
                              convert_to_float(row[4]), convert_to_float(row[5])))
                print(f"Dados de {csv_file} inseridos com sucesso!")
        conn.commit()
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.release_connection(conn)

def insert_operadoras_saude(csv_file):
    conn = db.get_connection()
    try:
        with conn.cursor() as cursor:
            with open(csv_file, encoding='utf-8') as f:
                total_lines = sum(1 for line in f) - 1
            
            with open(csv_file, encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                next(reader)  
                for row in tqdm(reader, total=total_lines, desc=f"Inserindo {os.path.basename(csv_file)}"):
                    cursor.execute('''
                        INSERT INTO operadoras_saude (
                            registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
                            logradouro, numero, complemento, bairro, cidade, uf, cep,
                            ddd, telefone, fax, endereco_eletronico, representante,
                            cargo_representante, regiao_de_comercializacao, data_registro_ans
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        convert_to_int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6],
                        row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                        row[15], row[16], row[17], convert_to_int(row[18]), row[19]
                    ))
        conn.commit()
        print(f"Dados de {csv_file} inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.release_connection(conn)      
# if __name__ == "__main__":
#     demonstracoes_files = [
#         "dados/1T2023.csv",
#         "dados/2T2023.csv",
#         "dados/3T2023.csv",
#         "dados/4T2023.csv",
#         "dados/1T2024.csv",
#         "dados/2T2024.csv",
#         "dados/3T2024.csv",
#         "dados/4T2024.csv",
#     ]
#     insert_demonstracoes_contabeis(demonstracoes_files)
#     insert_operadoras_saude("dados/Relatorio_cadop.csv")