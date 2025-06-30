import requests
import pandas
import pandas as pd
from datetime import datetime, timedelta
import os


print ("Inciando Script")

# Definição do período
data_final = datetime.now()

data_final = datetime(2025, 6, 28)
data_inicial = data_final - timedelta(days=10*365)

# Formatar data
data_final_formatada = data_final.strftime('%m-%d-%Y')
data_inicial_formatada = data_inicial.strftime('%m-%d-%Y')

# Período da busca
print(f"Buscando dados de {data_inicial_formatada} até {data_final_formatada}.")

#Construção da rota/URL da API
url_base = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"

url_completa = f"{url_base}?@dataInicial='{data_inicial_formatada}'&@dataFinalCotacao='{data_final_formatada}'&$format=json&$top=10000"

print("URL constituída. Fazendo requisição à API do Banco Central")

try:
    resposta = requests.get(url_completa)

    # Verifica que a requisição foi bem sucedida
    if resposta.status_code == 200:
        print("Requisição bem sucedida. Processando dados...")

        # Extrai os dados em formato JSON
        dados_json = resposta.json()

        # O JSON retornado pelo BCB tem uma chave "value"
        lista_de_cotacoes = dados_json['value']

        # Converte a lista para um DataFrame do Pandas
        df = pd.DataFrame(lista_de_cotacoes)

        print(f"Dados convertidos para tabela. Registros encontrados {len(df)}.")

        # Difine pasta destino
        nome_pasta = "raw"

        # Criar pasta caso não exista
        os.makedirs(nome_pasta, exist_ok=True)

        caminho_arquivo_csv = os.path.join(nome_pasta, "cotacao_dolar_ultimos_10_anos.csv")

        # index=False evita que o pandas salve o índice da tabela como uma coluna no arquivo
        df.to_csv(caminho_arquivo_csv, index=False, sep=';', decimal=',')

        print(f"Os dados foram salvos em {caminho_arquivo_csv}")

    else:
        # Se não retornar 200
        print(f"Erro na requisição: {resposta.status_code}")
        print(f"Resposta da API: {resposta.text}")

except Exception as e:
    print(f"Ocorreu um erro inesperado")