from flask import Flask, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os


load_dotenv() #carrega as variaveis de ambiente do arquivo .env
#Iniciação com o Flask
app = Flask(__name__, template_folder="app/templates")


app.secret_key = os.getenv("SECRET_KEY")

from app.routes.home import create_app
from app.routes.inscricoes import inscricoes_app

create_app(app)
inscricoes_app(app)

if __name__ == '__main__':
    app.run(debug=True)