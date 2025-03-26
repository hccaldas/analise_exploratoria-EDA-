# Análise Exploratória de Vendas

Este projeto realiza uma Análise exploratória de dados (EDA) em um conjunto de dados de vendas, utilizando bibliotecas como **Pandas**, **Matplotlib** e **Seaborn**. O objetivo é identificar padrões, tendências e insights úteis a partir dos dados.

## Funcionalidades

- Carregamento e limpeza de dados.
- Verificação de valores nulos e duplicados.
- Cálculo do ticket médio das vendas.
- Identificação dos produtos mais vendidos.
- Visualização de dados com gráficos de barras.
- Análise temporal e categórica (se as colunas necessárias existirem).

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Pandas**: Manipulação e análise de dados.
- **Matplotlib**: Criação de gráficos estáticos.
- **Seaborn**: Visualização de dados avançada.

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
   - Remoção de duplicados:
     ```python
     df.drop_duplicates(inplace=True)
     ```

4. **Cálculo do Ticket Médio**
   - O ticket médio é calculado com base no preço e na quantidade:
     ```python
     df["total_venda"] = df["price_y"] * df["quantity"]
     ticket_medio = df.groupby("sale_id")["total_venda"].mean()
     print("Ticket médio:", ticket_medio.mean())
     ```

5. **Produtos Mais Vendidos**
   - Identificação dos 10 produtos mais vendidos:
     ```python
     top_produtos = df['product'].value_counts().head(10)
     ```
   - Visualização com gráfico de barras:
     ```python
     import matplotlib.pyplot as plt
     import seaborn as sns

     plt.figure(figsize=(10, 5))
     sns.barplot(x=top_produtos.index, y=top_produtos.values)
     plt.title("Top 10 Produtos Mais Vendidos")
     plt.xlabel("Produto")
     plt.ylabel("Quantidade Vendida")
     plt.xticks(rotation=45)
     plt.show()
     ```

6. **Análise Temporal**
   - Conversão da coluna de data para o formato datetime:
     ```python
     df['created_at'] = pd.to_datetime(df['created_at'])
     ```

7. **Análise de Outliers**
   - Detecção de outliers com base nos preços:
     ```python
     sns.boxplot(x=df['price_y'])
     plt.title("Distribuição de Preços")
     plt.show()
     ```


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
