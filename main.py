import time
import random
from arvore import criar_indice_produto_arvore
from hashtable import criar_indice_produto_hash, obter_produto_completo_hash
from products import (
    inserir_produto, exibir_produtos, criar_indice_produto,
    pesquisa_binaria_produto, excluir_produto
)
from accesses import (
    inserir_acesso, exibir_acessos, excluir_acesso, criar_acessos_exemplo
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
            start_time = time.time()
            resultado = pesquisa_binaria_produto(id_busca)
            end_time = time.time()
            if resultado:
                print(f"Produto encontrado: ID: {resultado[0]}, Marca: {resultado[1]}, Nome: {resultado[2]}, Preço: {resultado[3]}")
            else:
                print("Produto não encontrado.")
            
            print(f"Tempo de busca binária: {end_time - start_time:.6f} segundos")
        
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
        print("4. Criar acessos de exemplo")
        print("5. Voltar ao menu principal")

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
            acessos_exemplo = [
                (1, 'S1', 'Olhou'),
                (2, 'S2', 'Comprou'),
                (1, 'S1', 'Olhou'),
                (2, 'S2', 'Comprou'),
                (54, '22', 'Olhou'),
                (65, 'S1', 'Comprou')
            ]
            criar_acessos_exemplo(acessos_exemplo)
            print("Acessos de exemplo criados com sucesso!")

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")
            
def menu_memoria():
    arvore_bplus = criar_indice_produto_arvore()  # Criar a árvore B+ na memória
    tabela_hash = criar_indice_produto_hash(campo_busca="marca")  # ou "nome" dependendo da escolha

    while True:
        print("\nMenu de Memória:")
        print("1. Exibir produtos")
        print("2. Consultar produto por ID (Índice Memória / árvore B+)")
        print("3. Consultar produto por ID (Tabela Hash)")
        print("4. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nProdutos:")
            exibir_produtos()
        
        elif opcao == "2":
            id_busca = input("Digite o ID do produto para buscar: ").upper()
            start_time = time.time()
            resultado = arvore_bplus.buscar(id_busca)  # Buscar o produto na árvore B+
            end_time = time.time()
            if resultado:
                id_produto, marca, nome, preco = resultado
                print(f"Produto encontrado: ID: {id_produto}, Marca: {marca}, Nome: {nome}, Preço: {preco:.2f}")
            else:
                print("Produto não encontrado.")
                
            print(f"Tempo de busca na árvore B+: {end_time - start_time:.6f} segundos")
        
        elif opcao == "3":
            print("\nConsulta na Tabela Hash:")
            chave_busca = input("Digite a Marca do produto para buscar: ")

            start_time = time.time()
            resultado = obter_produto_completo_hash(chave_busca, tabela_hash)  # Buscar o produto na tabela hash
            end_time = time.time()

            if resultado:
                id_produto, marca, nome, preco = resultado
                print(f"Produto encontrado: ID: {id_produto}, Marca: {marca}, Nome: {nome}, Preço: {preco:.2f}")
            else:
                print("Produto não encontrado.")
                
            print(f"Tempo de busca na Tabela Hash: {end_time - start_time:.6f} segundos")
        
        elif opcao == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Acessos")
        print("3. Gerenciar Memória")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_acessos()
        elif opcao == "3":
            menu_memoria()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# def gerar_proximo_id(id_atual):
#     """
#     Gera o próximo ID sequencial a partir de um ID passado, 
#     considerando o formato de IDs como A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ...
#     """
#     def incrementa_id(id_str):
#         # Incrementa o ID, considerando IDs com mais de duas letras após ZZ.
#         id_list = list(id_str)
#         i = len(id_list) - 1
#         while i >= 0:
#             if id_list[i] == 'Z':
#                 id_list[i] = 'A'
#                 i -= 1
#             else:
#                 id_list[i] = chr(ord(id_list[i]) + 1)
#                 break
        
#         # Caso o primeiro caractere tenha "zerado", inserimos uma nova letra à esquerda.
#         if id_list[0] == 'A' and len(id_list) > 1:
#             # Verifica se todos os caracteres estão como 'A' (indicando que devemos adicionar um novo nível).
#             if all(ch == 'A' for ch in id_list):
#                 id_list.insert(0, 'A')
        
#         return ''.join(id_list)

#     return incrementa_id(id_atual)

# def gerar_produtos_exemplo():
#     # Lista de marcas e modelos para criar produtos
#     marcas = ["Apple", "Samsung", "Dell", "Sony", "Google", "LG", "Xiaomi", "Huawei", "Microsoft", "Lenovo"]
#     modelos = [
#         "iPhone 12", "Galaxy S21", "Inspiron 15", "PlayStation 5", "Pixel 5", 
#         "iPhone 13", "Galaxy Note 20", "MacBook Pro", "PlayStation 4", "Surface Laptop"
#     ]
    
#     # ID inicial (começando de 'ZV' conforme sua solicitação)
#     id_produto = 'ZV'
    
#     produtos = []
#     for i in range(100):
#         marca = random.choice(marcas)
#         nome = random.choice(modelos)
#         preco = round(random.uniform(1000.00, 5000.00), 2)  # Preço aleatório entre 1000.00 e 5000.00
#         produtos.append((id_produto, marca, nome, preco))
        
#         # Gera o próximo ID para o próximo produto
#         id_produto = gerar_proximo_id(id_produto)
    
#     return produtos

# def inserir_100_produtos():
#     produtos = gerar_produtos_exemplo()
#     for produto in produtos:
#         id_produto, marca, nome, preco = produto
#         # Usar a função de inserção do produto
#         inserir_produto(id_produto, marca, nome, preco)
#         print(f"Produto {id_produto} inserido: {marca} - {nome} - R${preco:.2f}")
    
#     # Exibe uma mensagem de conclusão
#     print("100 produtos inseridos com sucesso!")

if __name__ == "__main__":
    # inserir_100_produtos()
    
    menu_principal()
