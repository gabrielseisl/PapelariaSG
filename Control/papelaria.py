import mysql.connector
from cadastro_fabricante import inserir_dados_fabricante
from exibir_fabricante import exibir_dados_fabricante
from cadastro_produto import inserir_dados_produto
from exibir_produto import exibir_dados_produto
from cadastro_fornecedor import inserir_dados_fornecedor
from exibir_fornecedor import exibir_dados_fornecedor
from cadastro_pedido import inserir_dados_pedido
from exibir_pedido import exibir_dados_pedido
from cadastro_estoque_cd import inserir_dados_estoque_cd
from exibir_estoque_cd import exibir_dados_estoque_cd
from cadastro_loja import inserir_dados_loja
from exibir_loja import exibir_dados_loja
from cadastro_estoque_loja import inserir_dados_estoque_loja
from exibir_estoque_loja import exibir_dados_estoque_loja
from cadastro_categoria import inserir_dados_categoria
from exibir_categoria import exibir_dados_estoque_categoria
from cadastro_movimentacao import inserir_dados_movimentacao
from exibir_movimentacao import exibir_dados_movimentacao
from cadastro_venda import inserir_dados_vendas
from exibir_venda import exibir_vendas

while True:

    print("\n===== PAPELARIA SG =====")
    print("1 - Fabricante")
    print("2 - Produto")
    print("3 - Fornecedor")
    print("4 - Pedido")
    print("5 - Estoque CD")
    print("6 - Loja")
    print("7 - Estoque Loja")
    print("8 - Categoria")
    print("9 - Movimentação")
    print("10 - Venda")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        inserir_dados_fabricante()
        exibir_dados_fabricante()

    elif opcao == "2":
        inserir_dados_produto()
        exibir_dados_produto()

    elif opcao == "3":
        inserir_dados_fornecedor()
        exibir_dados_fornecedor()

    elif opcao == "4":
        inserir_dados_pedido()
        exibir_dados_pedido()

    elif opcao == "5":
        inserir_dados_estoque_cd()
        exibir_dados_estoque_cd()

    elif opcao == "6":
        inserir_dados_loja()
        exibir_dados_loja()

    elif opcao == "7":
        inserir_dados_estoque_loja()
        exibir_dados_estoque_loja()

    elif opcao == "8":
        inserir_dados_categoria()
        exibir_dados_estoque_categoria()

    elif opcao == "9":
        inserir_dados_movimentacao()
        exibir_dados_movimentacao()

    elif opcao == "10":
        inserir_dados_vendas()
        exibir_vendas()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")




