import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def conectar():

        connection = psycopg2.connect(DATABASE_URL)
        return connection
    # try:

        
    # except psycopg2.Error as erro:
    #     erro = print(f"Erro ao conectar ao banco de dados: {erro}")
    #     return erro
