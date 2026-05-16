import mysql.connector

def conectar():
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="09lksys09@A",
        database="papelariasg"
    )
    print("conectado")
    return conexao
