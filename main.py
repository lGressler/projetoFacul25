import struct
import os

# Definindo a estrutura dos dados para o arquivo de produtos
produto_struct = struct.Struct("10s 20s 30s f")  # ID (10 bytes), Marca (20 bytes), Nome (30 bytes), Preço (4 bytes)
access_struct = struct.Struct("10s 10s 20s")     # ID (10 bytes), ID sessão (10 bytes), Ação (20 bytes)

# Arquivos
produto_file = 'produtos.bin'
index_file = 'index_produtos.bin'
access_file = 'acessos.bin'
access_index_file = 'index_acessos.bin'

# Funções para manipulação dos dados binários

def inserir_produto(id_produto, marca, nome, preco):
    """
    Insere um novo produto ordenado pelo ID no arquivo binário.
    """
    with open(produto_file, "ab") as f:
        registro = produto_struct.pack(id_produto.encode('utf-8'), marca.encode('utf-8'), 
                                       nome.encode('utf-8'), preco)
        f.write(registro)

def exibir_produtos():
    """
    Exibe todos os produtos do arquivo binário.
    """
    with open(produto_file, "rb") as f:
        while chunk := f.read(produto_struct.size):
            id_produto, marca, nome, preco = produto_struct.unpack(chunk)
            print(f"ID: {id_produto.decode().strip()}, Marca: {marca.decode().strip()}, "
                  f"Nome: {nome.decode().strip()}, Preço: {preco}")

def criar_indice_produto():
    """
    Cria um índice parcial para o campo chave (ID).
    """
    indices = []
    with open(produto_file, "rb") as f:
        offset = 0
        while chunk := f.read(produto_struct.size):
            id_produto, _, _, _ = produto_struct.unpack(chunk)
            indices.append((id_produto.decode().strip(), offset))
            offset += produto_struct.size
    with open(index_file, "wb") as index_f:
        for id_produto, offset in indices:
            index_f.write(f"{id_produto},{offset}\n".encode())

def pesquisa_binaria_produto(id_busca):
    """
    Pesquisa um produto pelo ID usando pesquisa binária no índice.
    """
    with open(index_file, "rb") as f:
        indices = [line.decode().strip().split(",") for line in f]
        low, high = 0, len(indices) - 1
        while low <= high:
            mid = (low + high) // 2
            id_produto, offset = indices[mid]
            if id_produto == id_busca:
                with open(produto_file, "rb") as prod_f:
                    prod_f.seek(int(offset))
                    chunk = prod_f.read(produto_struct.size)
                    id_produto, marca, nome, preco = produto_struct.unpack(chunk)
                    return (id_produto.decode().strip(), marca.decode().strip(), 
                            nome.decode().strip(), preco)
            elif id_produto < id_busca:
                low = mid + 1
            else:
                high = mid - 1
    return None

def inserir_acesso(id_acesso, id_sessao, acao):
    """
    Insere um novo acesso ordenado pelo ID no arquivo binário.
    """
    with open(access_file, "ab") as f:
        registro = access_struct.pack(id_acesso.encode('utf-8'), id_sessao.encode('utf-8'), 
                                      acao.encode('utf-8'))
        f.write(registro)

def exibir_acessos():
    """
    Exibe todos os acessos do arquivo binário.
    """
    with open(access_file, "rb") as f:
        while chunk := f.read(access_struct.size):
            id_acesso, id_sessao, acao = access_struct.unpack(chunk)
            print(f"ID Acesso: {id_acesso.decode().strip()}, ID Sessão: {id_sessao.decode().strip()}, "
                  f"Ação: {acao.decode().strip()}")

# Teste de inserção e exibição
inserir_produto("1", "Samsung", "Galaxy S21", 799.99)
inserir_produto("2", "Apple", "iPhone 12", 999.99)
exibir_produtos()

inserir_acesso("1", "S1", "Olhou")
inserir_acesso("2", "S2", "Comprou")
exibir_acessos()

# Criando e testando índice e pesquisa
criar_indice_produto()
resultado = pesquisa_binaria_produto("1")
if resultado:
    print(f"Produto encontrado: {resultado}")
else:
    print("Produto não encontrado.")
