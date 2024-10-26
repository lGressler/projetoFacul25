import struct

# Definindo a estrutura dos dados para o arquivo de produtos
produto_struct = struct.Struct("10s 20s 30s f ?")  # ID (10 bytes), Marca (20 bytes), Nome (30 bytes), Preço (4 bytes), Excluído (1 byte)
produto_file = 'produtos.bin'
index_file = 'index_produtos.bin'

def pad_string(value, length):
    """
    Preenche o valor com espaços até o tamanho fixo especificado.
    """
    return value.ljust(length)

def inserir_produto(id_produto, marca, nome, preco):
    """
    Insere um novo produto no arquivo binário.
    Atualiza o índice.
    """
    id_produto = pad_string(id_produto, 10)
    marca = pad_string(marca, 20)
    nome = pad_string(nome, 30)

    with open(produto_file, "ab") as f:
        registro = produto_struct.pack(id_produto.encode('utf-8'), 
                                       marca.encode('utf-8'), 
                                       nome.encode('utf-8'), 
                                       float(preco), 
                                       False)
        f.write(registro)
    
    # Atualiza o índice após a inserção
    criar_indice_produto()

def exibir_produtos():
    """
    Exibe todos os produtos do arquivo binário.
    """
    print("Produtos:")
    with open(produto_file, "rb") as f:
        while True:
            chunk = f.read(produto_struct.size)
            if len(chunk) < produto_struct.size:
                break  # Se o chunk lido for menor do que o esperado, saia do loop
            try:
                id_produto, marca, nome, preco, excluido = produto_struct.unpack(chunk)
                if not excluido:  # Exibe apenas os produtos não excluídos logicamente
                    # Decodifica os valores, garantindo que a operação seja segura
                    id_produto = id_produto.decode('utf-8').strip()
                    marca = marca.decode('utf-8').strip()
                    nome = nome.decode('utf-8').strip()
                    print(f"ID: {id_produto}, Marca: {marca}, Nome: {nome}, Preço: {preco:.2f}")
            except (UnicodeDecodeError, struct.error) as e:
                print(f"Erro ao ler o registro: {e}")

def criar_indice_produto():
    """
    Cria um índice parcial para o campo chave (ID) e salva em um arquivo binário.

    Permite que a busca seja mais rapida
    """
    indices = []
    with open(produto_file, "rb") as f:
        offset = 0
        while True:
            chunk = f.read(produto_struct.size)
            if len(chunk) < produto_struct.size:
                break  # Para ao ler dados menores que o tamanho esperado
            id_produto, _, _, _, excluido = produto_struct.unpack(chunk)
            if not excluido:  # Apenas adiciona ao índice se não estiver excluído logicamente
                indices.append((id_produto.decode().strip(), offset))
            offset += produto_struct.size

    # Imprimindo os índices para depuração
    print("Índices criados:")
    for id_produto, offset in indices:
        print(f"ID: {id_produto}, Offset: {offset}")

    with open(index_file, "wb") as index_f:
        for id_produto, offset in indices:
            index_f.write(f"{id_produto},{offset}\n".encode())

def pesquisa_binaria_produto(id_busca):
    """
    Pesquisa um produto pelo ID usando pesquisa binária no índice.
    """
    with open(index_file, "rb") as f:
        indices = [line.decode().strip().split(",") for line in f]
        print("Índices disponíveis para pesquisa:")
        for id_produto, offset in indices:
            print(f"ID: {id_produto}, Offset: {offset}")
        low, high = 0, len(indices) - 1
        while low <= high:
            mid = (low + high) // 2
            id_produto, offset = indices[mid]
            id_produto = id_produto.strip()  # Garantindo que não haja espaços extras
            if id_produto == id_busca:
                with open(produto_file, "rb") as prod_f:
                    prod_f.seek(int(offset))
                    chunk = prod_f.read(produto_struct.size)
                    if len(chunk) == produto_struct.size:  # Verifica se o chunk tem o tamanho esperado
                        id_produto, marca, nome, preco, excluido = produto_struct.unpack(chunk)
                        if not excluido:
                            return (id_produto.decode().strip(), marca.decode().strip(), 
                                    nome.decode().strip(), preco)
            elif id_produto < id_busca:
                low = mid + 1
            else:
                high = mid - 1
    return None

def excluir_produto(id_produto):
    """
    Exclui logicamente um produto pelo ID e atualiza o índice.
    """
    produtos_temp = []
    with open(produto_file, "rb") as f:
        while True:
            chunk = f.read(produto_struct.size)
            if len(chunk) < produto_struct.size:
                break  # Para ao ler dados menores que o tamanho esperado
            registro = produto_struct.unpack(chunk)
            if registro[0].decode().strip() == id_produto:
                # Marca como excluído --> exclusão lógica
                produtos_temp.append((registro[0], registro[1], registro[2], registro[3], True))
            else:
                produtos_temp.append(registro)

    # Reescreve o arquivo com os registros atualizados
    with open(produto_file, "wb") as f:
        for registro in produtos_temp:
            f.write(produto_struct.pack(*registro))
    
    # Atualiza o índice após exclusão
    criar_indice_produto()
