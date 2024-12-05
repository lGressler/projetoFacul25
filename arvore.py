import struct

produto_struct = struct.Struct("10s 20s 30s f ?")  # ID (10 bytes), Marca (20 bytes), Nome (30 bytes), Preço (4 bytes), Excluído (1 byte)
produto_file = 'produtos.bin'

class Nodo:
    def __init__(self, grau):
        self.grau = grau  # Grau da árvore
        self.chaves = []  # Lista de chaves (IDs dos produtos)
        self.pontos = []  # Lista de ponteiros (offsets dos produtos ou filhos)
        self.folhas = True  # Define se o nó é folha ou não

class ArvoreBPlus:
    def __init__(self, grau=2):
        self.grau = grau  # Grau da árvore
        self.raiz = Nodo(grau)  # Raiz inicial
        self.raiz.folhas = True  # A raiz começa como uma folha

    def inserir(self, id_produto, offset):
        """
        Insere uma chave (ID de produto) e o respectivo offset na árvore B+.
        Se a raiz estiver cheia, ela será dividida.
        """
        raiz = self.raiz
        if len(raiz.chaves) == (self.grau - 1):  # Verifica se a raiz está cheia
            # Se a raiz estiver cheia, a árvore cresce em altura
            novo_nodo = Nodo(self.grau)
            novo_nodo.folhas = False
            novo_nodo.pontos.append(self.raiz)  # O nó anterior vira um filho do novo nó
            self.raiz = novo_nodo
            self._dividir_nodo(self.raiz, 0)  # Dividindo o nó raiz
        self._inserir_no(self.raiz, id_produto, offset)

    def _inserir_no(self, nodo, id_produto, offset):
        """
        Insere um ID e seu respectivo offset no nó correto.
        """
        if nodo.folhas:  # Se for nó folha, insere diretamente
            i = 0
            while i < len(nodo.chaves) and nodo.chaves[i] < id_produto:
                i += 1
            nodo.chaves.insert(i, id_produto)  # Insere a chave
            nodo.pontos.insert(i, offset)  # Insere o offset correspondente
        else:  # Se não for nó folha, navegar recursivamente
            i = 0
            while i < len(nodo.chaves) and nodo.chaves[i] < id_produto:
                i += 1
            self._inserir_no(nodo.pontos[i], id_produto, offset)

    def _dividir_nodo(self, nodo, indice):
        """
        Divide o nó quando ele fica cheio, criando dois nós filhos.
        """
        grau = self.grau
        if len(nodo.chaves) < grau:  # Verifica se o nó tem chaves suficientes para ser dividido
            return  # Não faz nada se o nó não tem chaves suficientes para dividir

        meio = len(nodo.chaves) // 2  # Encontrar o meio para dividir
        chave_promovida = nodo.chaves[meio]

        novo_nodo = Nodo(grau)
        novo_nodo.folhas = nodo.folhas

        # Dividindo as chaves entre os dois nós
        novo_nodo.chaves = nodo.chaves[meio + 1:]
        nodo.chaves = nodo.chaves[:meio]

        # Dividindo os ponteiros entre os dois nós
        novo_nodo.pontos = nodo.pontos[meio + 1:]
        nodo.pontos = nodo.pontos[:meio + 1]

        # Atualizando a raiz
        if nodo == self.raiz:  # Se o nó a ser dividido for a raiz
            nodo.folhas = False  # A raiz não é mais uma folha
            nodo.chaves.append(chave_promovida)  # A chave do meio é promovida
            nodo.pontos.append(novo_nodo)  # O novo nó é adicionado à raiz
        else:
            # Caso o nó não seja raiz
            nodo.chaves.append(chave_promovida)
            nodo.pontos.append(novo_nodo)

        nodo.chaves.sort()  # Garantindo que as chaves na árvore estão ordenadas

    def buscar(self, id_produto):
        """
        Busca um produto na árvore B+ pela chave (ID) e retorna um conjunto completo de informações do produto.
        """
        nodo = self.raiz
        # Realiza a busca pela chave na árvore
        offset = self._buscar_no(nodo, id_produto)
        
        if offset:
            # Aqui você acessaria o arquivo binário para buscar os detalhes do produto
            print("OFFSET PRINT --> ", offset)
            produto = obter_produto_completo(offset)  # Função que recupera os detalhes completos do produto
            return produto  # Retorna todas as informações do produto
        else:
            return None

    def _buscar_no(self, nodo, id_produto):
        """
        Realiza a busca recursiva no nó, verificando se o ID está na chave.
        """
        i = 0
        while i < len(nodo.chaves) and nodo.chaves[i] < id_produto:
            i += 1

        # Verifica se encontrou o ID no nó
        if i < len(nodo.chaves) and nodo.chaves[i] == id_produto:
            return nodo.pontos[i]  # Retorna o offset do produto
        elif nodo.folhas:
            return None  # Se o nó for folha e não encontrar, retorna None
        else:
            return self._buscar_no(nodo.pontos[i], id_produto)  # Busca recursiva nos filhos

# Atualizando a função de criar o índice para usar uma árvore B+ em memória
def criar_indice_produto_arvore():
    indices = []
    with open(produto_file, "rb") as f:
        offset = 0
        while True:
            chunk = f.read(produto_struct.size)
            if len(chunk) < produto_struct.size:
                break
            id_produto, _, _, _, excluido = produto_struct.unpack(chunk)
            if not excluido:
                indices.append((id_produto.decode().strip(), offset))
            offset += produto_struct.size

    # Criando a árvore B+ em memória
    arvore_bplus = ArvoreBPlus()
    for id_produto, offset in indices:
        arvore_bplus.inserir(id_produto, offset)

    return arvore_bplus

def obter_produto_completo(offset):
    """
    A função recebe o offset (posição no arquivo binário) e retorna os detalhes completos do produto.
    """
    try:
        # Abre o arquivo binário no modo leitura
        with open(produto_file, "rb") as arquivo:
            # Move o ponteiro do arquivo para o offset especificado
            arquivo.seek(offset)
            
            # Lê os dados do produto com o tamanho da estrutura
            dados = arquivo.read(produto_struct.size)  # Lê o tamanho correto de bytes com base na estrutura
            
            if len(dados) == 0:
                return None  # Se não encontrar dados, retorna None
            
            # Desempacota os dados lidos de acordo com o formato definido
            id_produto, marca, nome, preco, excluido = produto_struct.unpack(dados)
            
            # Decodifica os valores para strings e float, e remove espaços em branco
            id_produto = id_produto.decode("utf-8").strip()
            marca = marca.decode("utf-8").strip()
            nome = nome.decode("utf-8").strip()
            preco = round(preco, 2)
            
            # Retorna as informações do produto
            return id_produto, marca, nome, preco
    except Exception as e:
        print(f"Erro ao acessar o arquivo: {e}")
        return None
