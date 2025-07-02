import pandas as pd
import os

print("Iniciando script de limpeza e transformação dos dados...")

#Leitura dos dados
caminho_arquivo_raw = os.path.join("raw", "cotacao_dolar_ultimos_10_anos.csv")

#Tenta ler o arquivo .csv. Tratar caso o arquivo não exista
try:
    df = pd.read_csv(caminho_arquivo_raw, sep=';', decimal=',')
    print("Arquivo CSV lido!")

except FileNotFoundError:
    print(f"Erro: o arquivo {caminho_arquivo_raw} não encontrado")
    print("Execute o script 'ingerir_cotacao_dolar.py' primeiro")
    exit() #encerra o script se o arquivo não existir

#Olhar os dados depois de carregar
print("\n--- Primeiras 5 linhas dos dados brutos ---")
print(df.head())

print("\n--- Informações sobre os tipos de dados ---")
df.info()

print("\nIniciando a limpeza e transformação...")

#Converte a coluna para o tipo datetime
df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'])

print("\nColuna 'dataHoraCotacao' convertida para o tipo datetime.")

# Formata a data como um texto no padrão que quisermos.
df['data_criacao'] = df['dataHoraCotacao'].dt.strftime('%Y-%m-%d')

df['hora_criacao'] = df['dataHoraCotacao'].dt.strftime('%H:%M')

print("Colunas 'data_criacao' e 'hora_criacao' criadas.")

print("\n--- Primeiras 5 linhas dos dados transformados ---")
# Mostramos as colunas relevantes para ver a transformação
print(df[['dataHoraCotacao', 'data_criacao', 'hora_criacao']].head())

# Define o nome da pasta de destino
nome_pasta_staging = "staging"

# Cria a pasta "staging" se ela não existir
os.makedirs(nome_pasta_staging, exist_ok=True)

# Define o caminho do novo arquivo
caminho_arquivo_staging = os.path.join(nome_pasta_staging, "cotacao_dolar_tratada.csv")

# Salva o DataFrame transformado em um novo arquivo .csv
df.to_csv(caminho_arquivo_staging, index=False, sep=';', decimal=',')

print(f"\nSucesso! Os dados limpos foram salvos em: {caminho_arquivo_staging}")