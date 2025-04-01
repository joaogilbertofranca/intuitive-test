# Projeto de Inserção de Dados em PostgreSQL - Intuitive Test

Este projeto em Python realiza a criação de tabelas e a inserção de dados em um banco de dados PostgreSQL a partir de arquivos CSV. Ele é estruturado para ser facilmente configurado e executado em diferentes máquinas usando uma virtual environment (venv) e Docker para o banco de dados.

## Estrutura do Projeto

- **`venv/`**: Pasta contendo o ambiente virtual Python (criada localmente, não versionada).
- **`dados/`**: Pasta com os arquivos CSV necessários para o projeto:
  - `1T2023.csv`, `2T2023.csv`, `3T2023.csv`, `4T2023.csv`
  - `1T2024.csv`, `2T2024.csv`, `3T2024.csv`, `4T2024.csv`
  - `Relatorio_cadop.csv`
- **`db.py`**: Script para conexão com o banco de dados PostgreSQL.
- **`create_tables.py`**: Script para criar as tabelas no banco de dados.
- **`insert_data.py`**: Script para inserir os dados dos CSVs nas tabelas.
- **`main.py`**: Script principal para executar `create_tables.py` e `insert_data.py` na ordem correta.
- **`requirements.txt`**: Arquivo com as dependências Python do projeto.
- **`docker-compose.yml`**: Arquivo para configurar e iniciar o container do PostgreSQL.

## Pré-requisitos

- Python 3.8 ou superior instalado.
- Docker e Docker Compose instalados (para o banco de dados).
- Git (opcional, para clonar o repositório).

## Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto em uma nova máquina:

### 1. Clone o Repositório (se aplicável)
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>