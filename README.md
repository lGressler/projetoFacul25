# Sistema de Gerenciamento de Produtos e Acessos

Este projeto implementa um sistema de gerenciamento para produtos e acessos em uma loja de e-commerce, utilizando arquivos binários e índices para otimizar a pesquisa e a manipulação de dados. O sistema permite a inserção, exclusão lógica e consulta de produtos e acessos de forma eficiente.

## Estrutura do Projeto

O projeto contém duas principais funcionalidades:

1. **Gerenciamento de Produtos**:
   - Armazenamento de informações sobre produtos em um arquivo binário.
   - Suporte à inserção, exibição e exclusão lógica de produtos.
   - Criação e atualização de um índice para acesso rápido aos produtos.

2. **Gerenciamento de Acessos**:
   - Registro de ações dos usuários no e-commerce.
   - Suporte à inserção, exibição e exclusão lógica de acessos.

## Estruturas de Dados

### Produtos

Os dados dos produtos são armazenados em um arquivo binário (`produtos.bin`) com a seguinte estrutura:

| Campo     | Tipo       | Tamanho |
|-----------|------------|---------|
| ID        | String     | 10 bytes|
| Marca     | String     | 20 bytes|
| Nome      | String     | 30 bytes|
| Preço     | Float      | 4 bytes |
| Excluído  | Boolean    | 1 byte  |

### Acessos

Os dados de acessos são armazenados em um arquivo binário (`acessos.bin`) com a seguinte estrutura:

| Campo       | Tipo       | Tamanho |
|-------------|------------|---------|
| ID          | String     | 10 bytes|
| ID Sessão   | String     | 10 bytes|
| Ação        | String     | 20 bytes|
| Excluído    | Boolean    | 1 byte  |

## Funcionalidades

### Produtos

- **Inserir Produto**: Adiciona um novo produto ao sistema. O índice é atualizado automaticamente.
- **Exibir Produtos**: Mostra todos os produtos cadastrados que não foram excluídos.
- **Criar Índice de Produtos**: Gera um índice para acesso rápido aos produtos.
- **Pesquisar Produto por ID**: Busca um produto específico pelo seu ID.
- **Excluir Produto**: Realiza a exclusão lógica de um produto, marcando-o como excluído.

### Acessos

- **Inserir Acesso**: Adiciona um novo registro de acesso ao sistema.
- **Exibir Acessos**: Mostra todos os acessos registrados que não foram excluídos.
- **Excluir Acesso**: Realiza a exclusão lógica de um acesso, marcando-o como excluído.

## Uso

Para executar o sistema, você deve ter Python instalado em sua máquina. Siga as etapas abaixo:

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
