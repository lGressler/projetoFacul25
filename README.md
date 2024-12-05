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
2. python com versão acima de 3.6.8
3. Comando para dar start na main --> python main.py

--------------------------------------------------------------------------------------------------

# Resumo do Trabalho de Implementação de Arquivos de Dados e Índices

## Objetivo Geral
Criar arquivos de dados e índices para uma organização sequencial-indexada utilizando dados de comportamento em um e-commerce.

## Contexto
- **Dataset**: Dados de acessos a um e-commerce durante 7 meses, incluindo informações de usuários, produtos e comportamentos (visualizações, compras, etc.).
- **Fonte do Dataset**: [Kaggle - E-commerce Behavior Data](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

## Atividades a Realizar

1. **Definição do Contexto a ser Explorando**:
   - Estabelecer o contexto do comportamento em e-commerce e as perguntas que serão respondidas com os dados.

2. **Montagem dos Arquivos de Dados**:
   - Criar pelo menos dois arquivos de dados:
     - **Arquivo de Produtos**: Contendo informações sobre produtos (ex.: ID, nome, preço).
     - **Arquivo de Acessos**: Contendo dados de acessos ao site (ex.: ID do acesso, ID do usuário, ID do produto).
   - **Estrutura dos Arquivos**:
     - Cada arquivo deve conter pelo menos três campos, incluindo um campo chave (não repetido) e um campo com informações repetidas.
     - Os dados devem ser organizados sequencialmente, preferencialmente pelo campo chave.
     - Os arquivos devem ser salvos em modo binário e os registros devem ter tamanho fixo.

3. **Implementação das Funções para Cada Arquivo de Dados**:
   - **Inserção de Dados**: Função que ordena e insere os dados.
   - **Exibição de Dados**: Função para mostrar os dados do arquivo.
   - **Pesquisa Binária**: Função para realizar a pesquisa binária no arquivo de índice.
   - **Consulta de Dados**: Função para consultar dados usando a pesquisa binária.

4. **Criação de Índices**:
   - Criar um arquivo de índice parcial para cada arquivo de dados.
   - Implementar uma função para consultar dados a partir do índice usando pesquisa binária.

5. **Inserção/Remoção de Dados e Reconstrução do Índice**:
   - Gerenciar a inserção de novos registros e a remoção de registros.
   - Definir se a reconstrução do índice ocorre após cada inserção/remoção ou segue um outro critério.

6. **Documentação e Postagem**:
   - Descrever os arquivos de dados e os arquivos de índices.
   - Criar um repositório no GitHub com o código-fonte, arquivos de dados e índices gerados.

----------------------------------------------------------------------------------------------

# Critérios de Avaliação

## 1. Implementação dos Arquivos de Dados
- **Descrição**: Avalia a implementação dos arquivos de dados.
- **Critérios**:
  - Explicação da forma como os arquivos foram implementados.
  - Detalhamento do processo de ordenação dos dados na apresentação.

## 2. Implementação dos Índices Parciais de Arquivos
- **Descrição**: Avalia a criação e utilização dos índices.
- **Critérios**:
  - Explicação da forma como os índices foram implementados.
  - Demonstração de como os índices são utilizados para consultas na apresentação.

## 3. Implementação de Inserção e Remoção de Dados
- **Descrição**: Avalia a estrutura para manipulação de dados.
- **Critérios**:
  - Estrutura lógica para inserção de novos registros.
  - Método de remoção de registros.
  - Estratégia para reorganização dos arquivos e índices após inserções ou remoções.

## 4. Apresentação
- **Descrição**: Avalia a apresentação das funcionalidades implementadas.
- **Critérios**:
  - Utilização da pesquisa binária nos arquivos de índices e de dados.
  - Demonstração do uso dos índices para consultas.
  - Explicação da forma como esses elementos foram implementados na apresentação.

## 5. Entrega do Material Solicitado
- **Descrição**: Avalia a entrega do material necessário.
- **Critérios**:
  - Upload do código fonte.
  - Descrição das estruturas dos índices e das consultas realizadas.
  - Disponibilização dos arquivos de dados e de índices no GitHub.