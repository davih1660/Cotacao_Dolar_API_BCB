# Importando o adaptador Psycopg2
import psycopg2

# Criando um dicionário com as variáveis necessárias para conexão ao Banco
pg_conn_dict = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '1234',
    'port': '5432',
    'host': 'localhost'
}

# Instanciando a conexão com o Banco
conn = psycopg2.connect(**pg_conn_dict)

# Definindo o cursor (objeto utilizado para executar comandos SQL)
cur = conn.cursor()

# Criando o Schema 
cur.execute("CREATE SCHEMA IF NOT EXISTS edumi;")

# Criando a tabela para armazenamento dos dados
cur.execute("""
    CREATE TABLE IF NOT EXISTS edumi.tbl_bcb (
	    id SERIAL PRIMARY KEY,
	    name TEXT NOT NULL,
	    AGE INT NOT NULL
    );    
"""
)

# Inserindo dados na tabela criada
cur.execute("""
    INSERT INTO edumi.tbl_bcb (name, age) VALUES (%s, %s)             
""", ('Josué Lui', 25) 
)

# Efetuando o commit das alterações
conn.commit()

# Fechando a comunicação com o banco de dados
cur.close()
conn.close()
