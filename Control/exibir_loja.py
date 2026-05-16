import mysql.connector
from conexao import conectar

def exibir_dados_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM LOJA")

        resultados = cursor.fetchall()

        print("\nLoja:")

        for id_loja, nome_loja, cnpj, endereco, telefone, gerente, id_estoque_cd in resultados:
            print(f"ID: {id_loja} | Nome: {nome_loja} | CNPJ: {str(cnpj)[:4]}****** | Endereço: {endereco[:10]}... | Telefone: *****-{str(telefone)[-4:]} | Gerente: {gerente} | ID estoque: {id_estoque_cd}")
        cursor.close()
        conexao.close()