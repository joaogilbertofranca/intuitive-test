from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

SWAGGER_URL = '/docs'  
API_URL = '/static/swagger.json'  
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Operadoras Saúde API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",  
        database="intuitive",  
        user="root",  
        password="root"  
    )
    return conn

@app.route('/api/buscar_operadoras', methods=['GET'])
def buscar_operadoras():
    termo_busca = request.args.get('termo', '')  
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM operadoras_saude 
        WHERE razao_social ILIKE %s 
        OR nome_fantasia ILIKE %s
        OR cnpj ILIKE %s
        OR cidade ILIKE %s
        LIMIT 10;
    """, (f'%{termo_busca}%', f'%{termo_busca}%', f'%{termo_busca}%', f'%{termo_busca}%'))
    
    registros = cur.fetchall()
    cur.close()
    conn.close()

    operadoras = []
    for registro in registros:
        operadoras.append({
            "id": registro[0],
            "registro_ans": registro[1],
            "cnpj": registro[2],
            "razao_social": registro[3],
            "nome_fantasia": registro[4],
            "modalidade": registro[5],
            "logradouro": registro[6],
            "numero": registro[7],
            "complemento": registro[8],
            "bairro": registro[9],
            "cidade": registro[10],
            "uf": registro[11],
            "cep": registro[12],
            "ddd": registro[13],
            "telefone": registro[14],
            "fax": registro[15],
            "endereco_eletronico": registro[16],
            "representante": registro[17],
            "cargo_representante": registro[18],
            "regiao_de_comercializacao": registro[19],
            "data_registro_ans": registro[20]
        })
    
    return jsonify(operadoras)

@app.route('/static/swagger.json')
def swagger_json():
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "Operadoras Saúde API",
            "version": "1.0.0",
            "description": "API para buscar operadoras de saúde"
        },
        "paths": {
            "/api/buscar_operadoras": {
                "get": {
                    "summary": "Busca operadoras de saúde",
                    "parameters": [
                        {
                            "name": "termo",
                            "in": "query",
                            "description": "Termo para buscar nas colunas `razao_social`, `nome_fantasia`, `cnpj` e `cidade`.",
                            "required": False,
                            "type": "string",
                            "example": "saúde"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Lista de operadoras de saúde encontradas.",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "registro_ans": {"type": "integer"},
                                        "cnpj": {"type": "string"},
                                        "razao_social": {"type": "string"},
                                        "nome_fantasia": {"type": "string"},
                                        "modalidade": {"type": "string"},
                                        "logradouro": {"type": "string"},
                                        "numero": {"type": "string"},
                                        "complemento": {"type": "string"},
                                        "bairro": {"type": "string"},
                                        "cidade": {"type": "string"},
                                        "uf": {"type": "string"},
                                        "cep": {"type": "string"},
                                        "ddd": {"type": "string"},
                                        "telefone": {"type": "string"},
                                        "fax": {"type": "string"},
                                        "endereco_eletronico": {"type": "string"},
                                        "representante": {"type": "string"},
                                        "cargo_representante": {"type": "string"},
                                        "regiao_de_comercializacao": {"type": "integer"},
                                        "data_registro_ans": {"type": "string", "format": "date"}
                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "Parâmetro de busca inválido"
                        }
                    }
                }
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
