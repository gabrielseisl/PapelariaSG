import mysql.connector
from conexao import conectar

def inserir_dados_pedido():

    conexao = conectar()
    
    if conexao:
        cursor = conexao.cursor()

        data_pedido = input("Data do pedido: ")
        data_entrega = input("Data da entrega: ")
        valor_total = input("Valor total: ")
        quantia_itens = input("Quantia de itens: ")
        entrega_status = input("Status da entrega: ")
        id_fornecedor = int(input("ID do fornecedor: "))

        sql = "INSERT INTO pedido (data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor)