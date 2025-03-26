# Projeto de Análise de Vendas

Este projeto realiza uma **análise exploratória de dados (EDA)** e integra os dados de vendas com um banco de dados MySQL. Ele é composto por diferentes arquivos que trabalham juntos para carregar, transformar, analisar e visualizar os dados.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

1. **`analise_vendas.ipynb`**:
   - Um notebook Jupyter que realiza a análise exploratória de dados (EDA).
   - Carrega os dados do arquivo `tudo.csv` para identificar padrões, tendências e insights.
   - Inclui análises como:
     - Produtos mais vendidos.
     - Ticket médio das vendas.
     - Análise temporal e categórica.
     - Detecção de outliers.

2. **`dashboard_despesas.py`**:
   - Um script que cria um dashboard interativo usando Streamlit.
   - Permite a visualização dinâmica dos dados de vendas.
   - Conecta-se ao mesmo conjunto de dados (`tudo.csv`) para fornecer uma interface interativa.

3. **`load.py`**:
   - Um script que carrega os dados do arquivo `tudo.csv` para um banco de dados MySQL.
   - Realiza transformações nos dados para garantir que eles estejam no formato correto antes de serem inseridos no banco.
   - Insere os dados na tabela `vendas` do banco de dados `vendas_db`.

---

## Conexão entre os Arquivos

### `load.py` e `analise_vendas.ipynb`
- O arquivo `load.py` é responsável por carregar os dados do arquivo `tudo.csv` para o banco de dados MySQL.
- O notebook `analise_vendas.ipynb` utiliza o mesmo arquivo `tudo.csv` para realizar a análise exploratória de dados.
- Ambos os arquivos trabalham com o mesmo conjunto de dados, mas `load.py` prepara os dados para serem armazenados no banco de dados, enquanto o notebook realiza a análise.

### `load.py` e `dashboard_despesas.py`
- O script `load.py` insere os dados no banco de dados MySQL.
- O script `dashboard_despesas.py` pode ser modificado para buscar os dados diretamente do banco de dados MySQL, em vez de usar o arquivo `tudo.csv`.

---

## Fluxo de Trabalho

1. **Carregamento e Transformação dos Dados (`load.py`)**:
   - O arquivo `load.py` carrega os dados do arquivo `tudo.csv`, realiza transformações e insere os dados no banco de dados MySQL.
   - Exemplo de execução:
     ```bash
     python load.py
     ```

2. **Análise Exploratória (`analise_vendas.ipynb`)**:
   - O notebook `analise_vendas.ipynb` realiza a análise exploratória diretamente no arquivo `tudo.csv`.
   - Exemplo de execução:
     ```bash
     jupyter notebook analise_vendas.ipynb
     ```

3. **Visualização Interativa (`dashboard_despesas.py`)**:
   - O script `dashboard_despesas.py` cria um dashboard interativo para explorar os dados.
   - Exemplo de execução:
     ```bash
     streamlit run dashboard_despesas.py
     ```

---

## Como Executar o Projeto

### 1. Configurar o Banco de Dados MySQL

1. Certifique-se de que o MySQL está instalado e em execução.
2. Crie o banco de dados `vendas_db` e a tabela `vendas`:
   ```sql
   CREATE DATABASE vendas_db;

   USE vendas_db;

   CREATE TABLE vendas (
       id_venda INT,
       cliente VARCHAR(255),
       email_cliente VARCHAR(255),
       id_produto INT,
       produto VARCHAR(255),
       preco_unitario FLOAT,
       quantidade INT,
       preco_total FLOAT,
       total_venda FLOAT,
       data_criacao DATETIME,
       data_atualizacao DATETIME
   );

#######3
1. instale as dependência:

pip install -r requirements.txt

2. Execute o notebook Jupyter:

jupyter notebook analise_vendas.ipynb

Estrutura do Projeto

├── analise_vendas.ipynb       # Notebook com a análise exploratória
├── tudo.csv                   # Arquivo de dados (não incluído no repositório)
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação do projeto
