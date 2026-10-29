
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Carrega o .env da raiz do projeto
pasta_projeto = Path(__file__).resolve().parent
load_dotenv(pasta_projeto / ".env")

chave = os.getenv("FOOTBALL_API_KEY")

if not chave:
    print("Chave não encontrada no arquivo .env")

else:
    try:
        resposta = requests.get(
            "https://api.football-data.org/v4/competitions",
            headers={"X-Auth-Token": chave},
            timeout=15
        )

        print("Status HTTP:", resposta.status_code)

        if resposta.status_code == 200:
            print("API conectada com sucesso!")

            dados = resposta.json()

            for competicao in dados.get("competitions", [])[:5]:
                print(competicao.get("name"))

        else:
            print("Resposta da API:", resposta.text[:500])

    except requests.RequestException as erro:
        print("Erro de conexão:", erro)
