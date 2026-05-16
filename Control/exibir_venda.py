
from conexao import conectar

def exibir_vendas():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM venda")
        resultados = cursor.fetchall()

        print("\n Vendas:")

        for id_venda, quantidade, preco_venda, lucro, forma_pagamento, data_venda, id_movimentacao in resultados:
            print(f"ID Venda: {id_venda} | Quantidade: {quantidade} | Preço Venda: {preco_venda} | Lucro: {lucro} | Forma Pagamento: {forma_pagamento} | Data Venda: {data_venda} | ID Movimentação: {id_movimentacao}")

        cursor.close()
        conexao.close()

