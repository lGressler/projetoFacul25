import struct

# Definindo a estrutura dos dados para o arquivo de acessos
access_struct = struct.Struct("10s 10s 20s")     # ID (10 bytes), ID sessão (10 bytes), Ação (20 bytes)
access_file = 'acessos.bin'

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
