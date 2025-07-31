# Script criado para rodar o Banco de dados Postgres via Terminal

# Comandos úteis 

## Para interromper o container em execução: docker stop postgres-edumi 

## Para startar o container: docker start postgres-edumi 

## Para restartar o container: docker restart postgres-edumi 

docker run -d  \
    --name postgres-edumi \
    -p 5432:5432 \
    -e POSTGRES_PASSWORD=1234 \
    postgres:latest
