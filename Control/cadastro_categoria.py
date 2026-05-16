import mysql.connector
from conexao import conectar

def inserir_dados_categoria():

    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()

        nome_categoria = input("Nome da categoria: ")
        descricao = input("Descrição: ")
        tipo = input("Tipo da categoria: ")
        data_cadastro = input("Data do cadastro: ")
        estampa = input("Estampa: ")
        id_estoque_loja = int(input("ID do estoque loja: "))

        sql = "INSERT INTO categoria (nome_categoria, descricao, tipo, data_cadastro, estampa, id_estoque_loja) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (nome_categoria, descricao, tipo, data_cadastro, estampa, id_estoque_loja)

        cursor.execute(sql, values)
        conexao.commit()

        print("Categoria inserida")

        cursor.close()
        conexao.close()