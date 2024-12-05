import struct

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
    def __init__(self, tamanho=100):
        self.tamanho = tamanho  # Define o tamanho da tabela hash
        self.tabela = [[] for _ in range(tamanho)]  # Inicializa a tabela com listas vazias

    def _hash(self, chave):
        """
        Função de hash simples baseada no valor do ID do produto.
        """
        return hash(chave) % self.tamanho

    def inserir(self, produto):
        """
        Insere um produto na tabela hash, usando o ID do produto como chave.
        """
        indice = self._hash(produto.id_produto)
        # Verifica se o produto já existe na tabela
        for item in self.tabela[indice]:
            if item.id_produto == produto.id_produto:
                return  # Produto já existe, não insere novamente
        # Adiciona o produto à tabela
        self.tabela[indice].append(produto)

    def buscar(self, id_produto):
        """
        Busca um produto na tabela hash pelo ID.
        """
        indice = self._hash(id_produto)
        for produto in self.tabela[indice]:
            if produto.id_produto == id_produto:
                return produto
        return None  # Produto não encontrado

    def exibir_tabela(self):
        """
        Exibe todos os produtos na tabela hash.
        """
        for i, lista in enumerate(self.tabela):
            if lista:  # Se houver elementos no índice
                for produto in lista:
                    print(produto)

# Função para criar o índice na tabela hash
def criar_indice_produto_hash():
    tabela_hash = TabelaHash()
    
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
                # O preço é um número float, então não tentamos decodificá-lo
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
def obter_produto_completo_hash(id_produto, tabela_hash):
    """
    A função recebe o ID do produto e retorna os detalhes completos do produto.
    """
    print("ID DO PRODUTO --> ", id_produto)
    produto = tabela_hash.buscar(id_produto)  # Chama o método buscar da instância
    if produto:
        return produto.id_produto, produto.marca, produto.nome, produto.preco
    else:
        return None
