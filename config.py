from dotenv import load_dotenv
import os

load_dotenv()  # carrega as variáveis do arquivo .env

omdb_api_key = os.getenv("OMDB_API_KEY")#valor da variável OMDB_API_KEY
