from products import inserir_produto, exibir_produtos, criar_indice_produto, pesquisa_binaria_produto
from accesses import inserir_acesso, exibir_acessos

# Menu para interagir com o sistema
def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir produto")
        print("2. Exibir todos os produtos")
        print("3. Criar índice de produtos")
        print("4. Pesquisar produto por ID")
        print("5. Inserir acesso")
        print("6. Exibir todos os acessos")
        print("7. Sair")

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
            id_acesso = input("ID do Acesso: ")
            id_sessao = input("ID da Sessão: ")
            acao = input("Ação realizada: ")
            inserir_acesso(id_acesso, id_sessao, acao)
            print("Acesso inserido com sucesso!")
        
        elif opcao == "6":
            print("\nAcessos:")
            exibir_acessos()
        
        elif opcao == "7":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()
