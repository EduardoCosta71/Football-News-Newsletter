from flask import Flask, render_template, redirect, url_for, session
import pyodbc
from app.database import get_db_connection


def create_app(app):

    @app.route("/")
    def home():


        return render_template('index.html')

    