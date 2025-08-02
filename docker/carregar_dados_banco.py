import requests
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# 1. Ingestão de Dados
url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='07-01-2025'&@dataFinalCotacao='08-01-2025'&$format=json&$top=100"
response = requests.get(url)
response.raise_for_status()
data = pd.DataFrame(response.json()['value'])[['cotacaoCompra', 'cotacaoVenda', 'dataHoraCotacao']]

# 2. Conexão e Carga no Banco
db_params = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "1234",
    "dbname": "edume"
}
conn = None
try:
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    cur.execute("CREATE SCHEMA IF NOT EXISTS bcb;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bcb.cotacao_dolar (
            id SERIAL PRIMARY KEY,
            cotacao_compra NUMERIC(10, 4),
            cotacao_venda NUMERIC(10, 4),
            data_hora_cotacao TIMESTAMP
        );
    """)

    tuples = [tuple(x) for x in data.to_numpy()]
    cols = ','.join(list(data.columns))
    query  = f"INSERT INTO bcb.cotacao_dolar ({cols}) VALUES %s"
    
    execute_values(cur, query, tuples)
    conn.commit()
except (Exception, psycopg2.Error) as error:
    if conn:
        conn.rollback()
finally:
    if conn:
        cur.close()
        conn.close()