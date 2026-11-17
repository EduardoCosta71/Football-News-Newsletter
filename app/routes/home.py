from flask import Flask, render_template, redirect, url_for, session
import pyodbc
from app.database import get_db_connection
from app.services.football_api import search_competitions, search_matches
from app.services.news_api import format_news, search_news


def create_app(app):

    @app.route("/")
    def home():

        noticias = search_news()  # Chama a função search_news() para obter as notícias

        noticias_formatadas = format_news(noticias)  # Formata as notícias para exibição

        partidas = search_matches()  # Chama a função search_matches() para obter as partidas

        competicoes = search_competitions()  # Chama a função search_competitions() para obter as competições

        return render_template('index.html', noticias=noticias_formatadas, partidas=partidas, competicoes=competicoes)  # Passa as notícias, partidas e competições formatadas para o template

    