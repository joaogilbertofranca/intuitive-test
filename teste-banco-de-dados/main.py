import create_tables
import insert_data
import consulta_analitica

def main():
    demonstracoes_files = [
        "dados/1T2023.csv",
        "dados/2T2023.csv",
        "dados/3T2023.csv",
        "dados/4T2023.csv",
        "dados/1T2024.csv",
        "dados/2T2024.csv",
        "dados/3T2024.csv",
        "dados/4T2024.csv",
    ]
    print("Iniciando a execução do projeto...")

    print("Criando tabelas no banco de dados...")
    create_tables.create_tables()

    print("Inserindo dados nas tabelas...")
    insert_data.insert_demonstracoes_contabeis(demonstracoes_files)
    insert_data.insert_operadoras_saude("dados/Relatorio_cadop.csv")

    print("Fazendo a consulta analítica...")
    consulta_analitica.execute_reports()

    print("Execução concluída com sucesso!")

if __name__ == "__main__":
    main()