import os
import requests
from dotenv import load_dotenv
from pathlib import Path


caminhar_env = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(caminhar_env)

API_KEY = os.getenv("GNEWS_API_KEY")
url = "https://gnews.io/api/v4"

def requeste(endpoint, parametros=None):

    """Requisição da API"""

    if not API_KEY:
        raise ValueError("A chave API não foi encontrada no .env")

    parametros = parametros or {}

    parametros["apikey"] = API_KEY


    resposta = requests.get(f"{url}/{endpoint}", params=parametros, timeout=10)

    resposta.raise_for_status()

    return resposta.json()



def search_news(assunto="futebol brasileiro"):

    """Pegando as noticias"""

    parametros = {
    
        "q": assunto,
        "lang": "pt",
        "country": "br",
        "max": 10

    }

    dados = requeste("search", parametros)

    return dados.get("articles", [])



def format_news(noticias):

    """Organizando as noticias"""

    noticias_formatadas = []

    for noticia in noticias:

        artigo = {

            "titulo": noticia.get("title"),
            "descricao": noticia.get("description"),
            "fonte": noticia.get("source", {}).get("name"),
            "imagem": noticia.get("image"),
            "data": noticia.get("publishedAt"),
            "link": noticia.get("url")

        }


        noticias_formatadas.append(artigo)

    return noticias_formatadas





