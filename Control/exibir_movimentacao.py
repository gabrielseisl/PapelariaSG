import mysql.connector
from conexao import conectar


def exibir_dados_movimentacao():

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM MOVIMENTACAO")
        resultados = cursor.fetchall()

        print("\nMovimentações:")

        for id_movimentacao, tipo, quantidade, origem, destino, data_movimentacao, id_categoria in resultados:
            print(f"ID: {id_movimentacao} | Tipo: {tipo} | Quantidade: {quantidade} | Origem: {origem} | Destino: {destino} | Data: {data_movimentacao} | ID Categoria: {id_categoria}")

        cursor.close()
        conexao.close()