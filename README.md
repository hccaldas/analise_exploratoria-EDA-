# Análise Exploratória de Vendas

Este projeto realiza uma análise exploratória de dados (EDA) em um conjunto de dados de vendas, utilizando bibliotecas como Pandas, Matplotlib e Seaborn. O objetivo é identificar padrões, tendências e insights úteis a partir dos dados.

## Funcionalidades

- Carregamento e limpeza de dados.
- Verificação de valores nulos e tratamento de dados ausentes.
- Ticket médio de vendas
- Análise das colunas principais, como produtos mais vendidos e frequência de vendas.
- Visualização de dados com gráficos interativos e estáticos.

## Tecnologias Utilizadas

- Python: Linguagem principal do projeto.
- Pandas: Manipulação e análise de dados.
- Matplotlib: Criação de gráficos estáticos.
- Seaborn: Visualização de dados avançada.

## Etapas da Análise Exploratória

1. **Carregamento dos Dados**
   - Os dados são carregados a partir de um arquivo CSV (`tudo.csv`).
   - Exemplo de código:
     ```python
     import pandas as pd
     df = pd.read_csv("tudo.csv", delimiter=";")
     ```

2. **Resumo dos Dados**
   - Exibição das primeiras linhas do DataFrame:
     ```python
     print(df.head())
     ```
   - Resumo das colunas e tipos de dados:
     ```python
     print(df.info())
     ```

3. **Tratamento de Dados**
   - Verificação de valores nulos:
     ```python
     print(df.isnull().sum())
     ```
   - Remoção de valores nulos:
     ```python
     df.dropna(inplace=True)
     ```

4. **Análise de Produtos Mais Vendidos**
   - Identificação dos 10 produtos mais vendidos:
     ```python
     top_products = df['Product'].value_counts().head(10)
     ```
   - Visualização com gráfico de barras:
     ```python
     import matplotlib.pyplot as plt
     import seaborn as sns

     plt.figure(figsize=(10, 5))
     sns.barplot(x=top_products.index, y=top_products.values)
     plt.title("Top 10 Produtos Mais Vendidos")
     plt.xlabel("Produto")
     plt.ylabel("Frequência")
     plt.show()
     ```

5. **Outras Análises**
   - Frequência de vendas por categoria.
   - Análise temporal (vendas por mês ou ano).
   - Identificação de outliers.


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
