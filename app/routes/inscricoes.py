from flask import Flask, render_template, redirect, url_for, session, request
import pyodbc
import re
from app.database import get_db_connection

def inscricoes_app(app):

    # Verificação de Email
    def validar_email(email):

        padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao_email, email) is not None

    #Verifica se email existe..
    def email_existe(email):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Inscritos WHERE Email = ?", (email,))
        inscrito = cursor.fetchone()

        conn.close()

        return inscrito is not None
    
#======================================================================================
    
    @app.route('/inscricao', methods=["GET", "POST"])
    def inscricao():

        if request.method == "POST":

            nome = request.form['nome']
            email = request.form['email']

            if not nome or not email:
                  return "Preencha o nome e o email", 400

            if not validar_email(email):
                    return "Email inválido. Por favor, insira um email válido.", 400


            if email_existe(email):
                    return "Este email já está inscrito.", 409

            conn = get_db_connection()

            try:
                 
                cursor = conn.cursor()

                cursor.execute("""INSERT INTO Inscritos
                              (Nome, Email) VALUES (?, ?)""",
                              (nome, email))

            
                conn.commit()

            finally: 
                conn.close()

            return redirect(url_for('inscricao'))

        return render_template('index.html')