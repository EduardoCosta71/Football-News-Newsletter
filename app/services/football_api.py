import os
import requests
from dotenv import load_dotenv
from pathlib import Path


caminho_env = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(caminho_env)

API_KEY = os.getenv("FOOTBALL_API_KEY")
url = "https://api.football-data.org/v4"


def request(endpoint, parametros=None):

    """Fazendo um requisição da API"""

    if not API_KEY:
        raise ValueError("A chave API não foi encontrada no .env")

    cabecalhos = {

        "X-Auth-Token": API_KEY

    }

    resposta = requests.get(f"{url}/{endpoint}", headers=cabecalhos, params=parametros, timeout=20)

    resposta.raise_for_status()

    return resposta.json()


# Função responsável por requisitar as competições disponíveis.
def search_competitions():
    """Retornar as competições disponíveis"""

    dados = request("competitions")

    return dados.get("competitions", [])


#Função responsvel por requisitar partidas.
def search_matches(code_competitions="BSA"):
    """Requisição das Partidas"""

    data = request(f"competitions/{code_competitions}/matches")


    return data.get("matches", [])

