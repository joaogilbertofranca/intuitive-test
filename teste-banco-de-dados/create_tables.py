from db import db

def create_tables():
    conn = db.get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
                    id SERIAL PRIMARY KEY,
                    data DATE,
                    reg_ans INTEGER,
                    cd_conta_contabil INTEGER,
                    descricao TEXT,
                    vl_saldo_inicial NUMERIC,
                    vl_saldo_final NUMERIC
                );
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS operadoras_saude (
                    id SERIAL PRIMARY KEY,
                    registro_ans INTEGER,
                    cnpj VARCHAR(20),
                    razao_social TEXT,
                    nome_fantasia TEXT,
                    modalidade TEXT,
                    logradouro TEXT,
                    numero TEXT,               
                    complemento TEXT,
                    bairro TEXT,
                    cidade TEXT,
                    uf VARCHAR(2),
                    cep VARCHAR(8),
                    ddd VARCHAR(2),
                    telefone TEXT,             
                    fax TEXT,                  
                    endereco_eletronico TEXT,
                    representante TEXT,
                    cargo_representante TEXT,
                    regiao_de_comercializacao INTEGER,
                    data_registro_ans DATE
                );
            ''')
            
            conn.commit()
            print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        db.release_connection(conn)

if __name__ == "__main__":
    create_tables()