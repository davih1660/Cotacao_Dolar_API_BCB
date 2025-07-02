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

    