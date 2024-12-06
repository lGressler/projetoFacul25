import struct
import time

produto_struct = struct.Struct("10s 20s 30s f ?")  # ID (10 bytes), Marca (20 bytes), Nome (30 bytes), Preço (4 bytes), Excluído (1 byte)
produto_file = 'produtos.bin'

class Produto:
    def __init__(self, id_produto, marca, nome, preco):
        self.id_produto = id_produto
        self.marca = marca
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"ID: {self.id_produto}, Marca: {self.marca}, Nome: {self.nome}, Preço: {self.preco}"

class TabelaHash:
    def __init__(self, tamanho=100, campo_busca="nome"):
        """
        A tabela hash será construída com base no campo de busca, que pode ser "marca" ou "nome".
        """
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.campo_busca = campo_busca  # Pode ser "marca" ou "nome"

    def _hash(self, chave):
        """
        Função de hash simples baseada no valor do campo de busca (marca ou nome).
        """
        return hash(chave) % self.tamanho

    def inserir(self, produto):
        """
        Insere um produto na tabela hash com base no campo de busca (marca ou nome).
        """
        chave_busca = getattr(produto, self.campo_busca)  # Obtém o valor do campo de busca (marca ou nome)
        indice = self._hash(chave_busca)
        # Verifica se o produto já existe na tabela
        for item in self.tabela[indice]:
            if getattr(item, self.campo_busca) == chave_busca:
                return  # Produto já existe, não insere novamente
        # Adiciona o produto à tabela
        self.tabela[indice].append(produto)

    def buscar(self, chave_busca):
        """
        Busca um produto na tabela hash pelo campo de busca (marca ou nome).
        """
        indice = self._hash(chave_busca)
        for produto in self.tabela[indice]:
            if getattr(produto, self.campo_busca) == chave_busca:
                return produto
        return None  # Produto não encontrado

    def exibir_tabela(self):
        """
        Exibe todos os produtos na tabela hash.
        """
        for i, lista in enumerate(self.tabela):
            if lista:
                for produto in lista:
                    print(produto)
                    
    def remover(self, chave_busca):
        """
        Remove um produto da tabela hash pelo campo de busca (marca ou nome).
        """
        indice = self._hash(chave_busca)
        for i, produto in enumerate(self.tabela[indice]):
            if getattr(produto, self.campo_busca) == chave_busca:
                # Produto encontrado e removido
                self.tabela[indice].pop(i)
                return True  # Produto removido com sucesso
        return False  # Produto não encontrado

# Função para criar o índice na tabela hash
def criar_indice_produto_hash(campo_busca="nome"):
    tabela_hash = TabelaHash(campo_busca=campo_busca)
    
    with open(produto_file, "rb") as f:
        offset = 0
        while True:
            chunk = f.read(produto_struct.size)
            if len(chunk) < produto_struct.size:
                break
            # Desempacota os dados do arquivo binário
            id_produto, marca, nome, preco, excluido = produto_struct.unpack(chunk)
            
            if not excluido:
                # Aqui, fazemos a correção: as variáveis `marca` e `nome` são byte-strings e precisam ser decodificadas
                id_produto = id_produto.decode().strip()  # Decodifica o ID para string
                marca = marca.decode().strip()  # Decodifica a marca para string
                nome = nome.decode().strip()  # Decodifica o nome para string
                preco = round(preco, 2)  # Formata o preço para 2 casas decimais
                
                # Cria o objeto Produto e insere na tabela hash
                produto = Produto(id_produto, marca, nome, preco)
                tabela_hash.inserir(produto)
            
            offset += produto_struct.size

    return tabela_hash

# Função para obter produto completo pela tabela hash
def obter_produto_completo_hash(chave_busca, tabela_hash):
    """
    A função recebe o campo de busca (marca ou nome) e retorna os detalhes completos do produto.
    """
    print(f"Buscando produto com {tabela_hash.campo_busca} --> ", chave_busca)
    produto = tabela_hash.buscar(chave_busca)  # Chama o método buscar da instância
    if produto:
        return produto.id_produto, produto.marca, produto.nome, produto.preco
    else:
        return None
    
def pad_string(value, length):
    """
    Preenche o valor com espaços até o tamanho fixo especificado.
    """
    return value.ljust(length)

def inserir_produto_hashtable(tabela_hash, id_produto, marca, nome, preco):
    """
    Insere um novo produto na tabela hash.
    Atualiza o índice.
    """
    
    id_produto = pad_string(id_produto, 10)
    marca = pad_string(marca, 20)
    
    # Verificar e garantir que 'nome' seja uma string
    if not isinstance(nome, str):
        nome = str(nome)  # Forçar conversão para string
    
    nome = pad_string(nome, 30)  # Agora podemos garantir que 'nome' é uma string
    
    # Registro do produto
    with open(produto_file, "ab") as f:
        registro = produto_struct.pack(id_produto.encode('utf-8'), 
                                       marca.encode('utf-8'), 
                                       nome.encode('utf-8'), 
                                       float(preco), 
                                       False)
        f.write(registro)
    
    # Inserir o produto na tabela hash
    produto = Produto(id_produto, marca, nome, preco)
    tabela_hash.inserir(produto)

    # Atualiza o índice após a inserção
    criar_indice_produto_hash(campo_busca="nome")
    
def excluir_produto_hashtable(tabela_hash, nome_produto):
    """
    Exclui logicamente um produto da tabela hash utilizando o nome do produto.
    """
    print(f"Excluindo Produto: {nome_produto}")
    
    # Atualizar arquivo binário para marcar o produto como excluído
    produtos_temp = []
    with open(produto_file, "rb") as f:
        while True:
            chunk = f.read(produto_struct.size)
            if len(chunk) < produto_struct.size:
                break
            registro = produto_struct.unpack(chunk)
            id_produto = registro[0].decode().strip()
            marca = registro[1].decode().strip()
            nome = registro[2].decode().strip()
            preco = registro[3]
            excluido = registro[4]
            
            # Se o nome corresponder ao nome que queremos excluir, marca como excluído logicamente
            if nome == nome_produto and not excluido:
                produtos_temp.append((id_produto.encode('utf-8'), marca.encode('utf-8'), nome.encode('utf-8'), preco, True))
            else:
                produtos_temp.append(registro)
    
    # Reescreve o arquivo com os registros atualizados
    with open(produto_file, "wb") as f:
        for registro in produtos_temp:
            f.write(produto_struct.pack(*registro))

    # Remover o produto da tabela hash
    tabela_hash.remover(nome_produto)

    # Atualiza o índice após a exclusão
    criar_indice_produto_hash(campo_busca="nome")