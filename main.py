from products import (
    inserir_produto, exibir_produtos, criar_indice_produto,
    pesquisa_binaria_produto, excluir_produto
)
from accesses import (
    inserir_acesso, exibir_acessos, excluir_acesso
)

def menu_produtos():
    while True:
        print("\nMenu de Produtos:")
        print("1. Inserir produto")
        print("2. Exibir todos os produtos")
        print("3. Criar índice de produtos")
        print("4. Pesquisar produto por ID")
        print("5. Excluir produto por ID")
        print("6. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_produto = input("ID do Produto: ")
            marca = input("Marca do Produto: ")
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            inserir_produto(id_produto, marca, nome, preco)
            print("Produto inserido com sucesso!")
        
        elif opcao == "2":
            print("\nProdutos:")
            exibir_produtos()
        
        elif opcao == "3":
            criar_indice_produto()
            print("Índice de produtos criado com sucesso!")
        
        elif opcao == "4":
            id_busca = input("Digite o ID do produto para buscar: ")
            resultado = pesquisa_binaria_produto(id_busca)
            if resultado:
                print(f"Produto encontrado: ID: {resultado[0]}, Marca: {resultado[1]}, Nome: {resultado[2]}, Preço: {resultado[3]}")
            else:
                print("Produto não encontrado.")
        
        elif opcao == "5":
            id_produto = input("ID do Produto para excluir: ")
            excluir_produto(id_produto)
            print("Produto excluído logicamente com sucesso!")

        elif opcao == "6":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_acessos():
    while True:
        print("\nMenu de Acessos:")
        print("1. Inserir acesso")
        print("2. Exibir todos os acessos")
        print("3. Excluir acesso por ID")
        print("4. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_acesso = input("ID do Acesso: ")
            id_sessao = input("ID da Sessão: ")
            acao = input("Ação realizada: ")
            inserir_acesso(id_acesso, id_sessao, acao)
            print("Acesso inserido com sucesso!")
        
        elif opcao == "2":
            print("\nAcessos:")
            exibir_acessos()
        
        elif opcao == "3":
            id_acesso = input("ID do Acesso para excluir: ")
            excluir_acesso(id_acesso)
            print("Acesso excluído logicamente com sucesso!")

        elif opcao == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Acessos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_acessos()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
