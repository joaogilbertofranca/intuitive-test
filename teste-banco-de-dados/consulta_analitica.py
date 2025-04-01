import psycopg2
from fpdf import FPDF
from db import db

def get_top_operadoras(query, params):
    conn = db.get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        db.release_connection(conn)

def generate_pdf(filename, title, data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, title, ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    for row in data:
        pdf.cell(0, 10, f"{row[0]} - R$ {row[1]:,.2f}", ln=True)
    pdf.output(filename)

def execute_reports():
    trimestre_query = """
        SELECT nome_fantasia, SUM(vl_saldo_final) AS total_despesas
        FROM demonstracoes_contabeis
        JOIN operadoras_saude ON demonstracoes_contabeis.reg_ans = operadoras_saude.registro_ans
        WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        AND data >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY nome_fantasia
        ORDER BY total_despesas DESC
        LIMIT 10;
    """
    
    ano_query = """
        SELECT nome_fantasia, SUM(vl_saldo_final) AS total_despesas
        FROM demonstracoes_contabeis
        JOIN operadoras_saude ON demonstracoes_contabeis.reg_ans = operadoras_saude.registro_ans
        WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        AND data >= CURRENT_DATE - INTERVAL '1 year'
        GROUP BY nome_fantasia
        ORDER BY total_despesas DESC
        LIMIT 10;
    """
    
    trimestre_data = get_top_operadoras(trimestre_query, ())
    ano_data = get_top_operadoras(ano_query, ())
    
    print("Top 10 operadoras com maiores despesas no último trimestre:")
    for row in trimestre_data:
        print(f"{row[0]} - R$ {row[1]:,.2f}")
    
    print("\nTop 10 operadoras com maiores despesas no último ano:")
    for row in ano_data:
        print(f"{row[0]} - R$ {row[1]:,.2f}")
    
    generate_pdf("relatorio_trimestre.pdf", "Top 10 Despesas - Último Trimestre", trimestre_data)
    generate_pdf("relatorio_ano.pdf", "Top 10 Despesas - Último Ano", ano_data)

if __name__ == "__main__":
    execute_reports()