import os
import requests
from dotenv import load_dotenv
from pathlib import Path


caminho_env = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(caminho_env)

API_KEY = os.getenv("FOOTBALL_API_KEY")

url = "https://api.football-data.org/v4/competitions"

def buscar_competicoes():

    if not API_KEY:
        raise ValueError("A chave API não foi encontrada no .env")

    cabecalhos = {

        "X-Auth-Token": API_KEY

    }


    reposta = requests.get(url, headers=cabecalhos, timeout=10)

    reposta.raise_for_status()

    return reposta.json()

