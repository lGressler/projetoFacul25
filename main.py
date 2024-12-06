from collections import defaultdict
import pickle
import struct
import time
import random
from arvore import criar_indice_produto_arvore, excluir_produto_arvore, inserir_produto_arvore
from hashtable import Produto, criar_indice_produto_hash, excluir_produto_hashtable, inserir_produto_hashtable, obter_produto_completo_hash
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
    tabela_hash = criar_indice_produto_hash(campo_busca="nome")

    while True:
        print("\nMenu de Memória:")
        print("1. Exibir produtos")
        print("2. Consultar produto por ID (Índice Memória / árvore B+)")
        print("3. Consultar produto por nome (Tabela Hash)")
        print("4. Inserir produto pela arvore (árvore B+)")
        print("5. Excluir produto pela arvore (árvore B+)")
        print("6. Inserir produto pela tabela hash")
        print("7. Excluir produto pela tabela hash")
        print("8. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
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
            chave_busca = input("Digite o nome do produto para buscar: ")

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
            print("\nInserir produto pela arvore (árvore B+):")
            id_produto = input("ID do Produto: ").upper()
            marca = input("Marca do Produto: ")
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            
            start_time = time.time()
            inserir_produto_arvore(arvore_bplus, id_produto, marca, nome, preco)
            end_time = time.time()
            
            print(f"Tempo de inserção na árvore B+: {end_time - start_time:.6f} segundos")
            
        elif opcao == "5":
            print("\nExcluir produto pela arvore (árvore B+):")
            id_produto = input("ID do Produto para excluir: ").upper()
            
            start_time = time.time()
            excluir_produto_arvore(arvore_bplus, id_produto)
            end_time = time.time()
            
            print(f"Tempo de exclusão na árvore B+: {end_time - start_time:.6f} segundos")
        
        elif opcao == "6":
            print("\nInserir produto pela tabela hash:")
            id_produto = input("ID do Produto: ").upper()
            marca = input("Marca do Produto: ")
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            
            start_time = time.time()
            inserir_produto_hashtable(tabela_hash, id_produto, marca, nome, preco)
            end_time = time.time()
            
            print(f"Tempo de inserção na Tabela Hash: {end_time - start_time:.6f} segundos")
            
        elif opcao == "7":
            print("\nExcluir produto pela tabela hash:")
            nome_produto = input("Nome do Produto para excluir: ")
            
            start_time = time.time()
            excluir_produto_hashtable(tabela_hash, nome_produto)
            end_time = time.time()
            
            print(f"Tempo de exclusão na árvore B+: {end_time - start_time:.6f} segundos")
            
        elif opcao == "8":
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

if __name__ == "__main__": 
    menu_principal()
