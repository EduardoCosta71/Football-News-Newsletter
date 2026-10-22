import pyodbc

def get_db_connection():
    #Função para estabelecer conexão com o banco de dados SQL Server
    return pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'  # Substitua pelo nome do seu servidor e instância
        'DATABASE=FootBallNewsDB;'  # Substitua pelo nome do seu banco de dados
        'Trusted_Connection=yes;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )