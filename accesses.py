import struct

# Definindo a estrutura dos dados para o arquivo de acessos
access_struct = struct.Struct("10s 10s 20s ?")  # ID (10 bytes), ID sessão (10 bytes), Ação (20 bytes), Excluído (1 byte)
access_file = 'acessos.bin'

def pad_string(value, length):
    """
    Preenche o valor com espaços até o tamanho fixo especificado.
    """
    return value.ljust(length)[:length]  # Garante que a string não exceda o comprimento

def inserir_acesso(id_acesso, id_sessao, acao):
    """
    Insere um novo acesso no arquivo binário.
    """
    id_acesso = pad_string(str(id_acesso), 10)
    id_sessao = pad_string(id_sessao, 10)
    acao = pad_string(acao, 20)
    
    with open(access_file, "ab") as f:
        registro = access_struct.pack(id_acesso.encode('utf-8'), id_sessao.encode('utf-8'), 
                                      acao.encode('utf-8'), False)
        f.write(registro)

def exibir_acessos():
    """
    Exibe todos os acessos do arquivo binário.
    """
    try:
        with open(access_file, "rb") as f:
            while True:
                chunk = f.read(access_struct.size)
                if len(chunk) < access_struct.size:
                    break  # Se o chunk lido for menor do que o esperado, saia do loop
                try:
                    id_acesso, id_sessao, acao, excluido = access_struct.unpack(chunk)
                    if not excluido:  # Exibe apenas acessos não excluídos logicamente
                        # Decodifica os valores, garantindo que a operação seja segura
                        id_acesso = id_acesso.decode('utf-8').strip()
                        id_sessao = id_sessao.decode('utf-8').strip()
                        acao = acao.decode('utf-8').strip()
                        print(f"ID Acesso: {id_acesso}, ID Sessão: {id_sessao}, Ação: {acao}")
                except (UnicodeDecodeError, struct.error) as e:
                    print(f"Erro ao ler o registro: {e}")
    except FileNotFoundError:
        print("Arquivo de acessos não encontrado.")

def excluir_acesso(id_acesso):
    """
    Exclui logicamente um acesso pelo ID.
    """
    acessos_temp = []
    try:
        with open(access_file, "rb") as f:
            while chunk := f.read(access_struct.size):
                if len(chunk) < access_struct.size:
                    print("Registro incompleto encontrado, pulando...")
                    continue  # Ignora chunks com tamanho menor que o esperado

                registro = access_struct.unpack(chunk)
                if registro[0].decode().strip() == str(id_acesso):
                    # Marca como excluído --> exclusão logica
                    acessos_temp.append((registro[0], registro[1], registro[2], True))
                else:
                    acessos_temp.append(registro)

        # Reescreve o arquivo com os registros atualizados
        with open(access_file, "wb") as f:
            for registro in acessos_temp:
                f.write(access_struct.pack(*registro))
        print("Acesso excluído logicamente com sucesso!")  # Confirmação de exclusão
    except FileNotFoundError:
        print("Arquivo de acessos não encontrado.")

def criar_acessos_exemplo(acessos):
    """
    Cria um arquivo de acessos exemplo, caso ele não exista.
    """
    try:
        with open(access_file, "xb") as f:  # 'x' para criar um novo arquivo
            for acesso in acessos:
                id_acesso, id_sessao, acao = acesso
                inserir_acesso(id_acesso, id_sessao, acao)
        print("Acessos de exemplo criados com sucesso!")
    except FileExistsError:
        print("O arquivo de acessos já existe.")

# Exemplo de acessos que você quer adicionar
acessos_exemplo = [
    (1, 'S1', 'Olhou'),
    (2, 'S2', 'Comprou'),
    (1, 'S1', 'Olhou'),
    (2, 'S2', 'Comprou'),
    (54, '22', 'Olhou'),
    (65, 'S1', 'Comprou')
]

# Executando a criação de acessos exemplo ao iniciar o script
criar_acessos_exemplo(acessos_exemplo)

# Exibindo acessos após a criação
exibir_acessos()
