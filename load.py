import mysql.connector
import pandas as pd

# Conectar ao MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",  # Se for um servidor remoto, substitua pelo IP
    user="root",  # Substituir pelo seu usuário MySQL
    password="Rastafari1@",  # Substituir pela sua senha MySQL
    database="vendas_db"
)
cursor = conn.cursor()

# Carregar os dados transformados
df = pd.read_csv("tudo.csv", encoding="ISO-8859-1")

# Renomear colunas para corresponder à tabela MySQL
df.rename(columns={
    "name": "cliente",
    "sale_id": "id_venda",
    "product_id": "id_produto",
    "product": "produto",
    "price_y": "preco_unitario",
    "quantity": "quantidade",
    "price_x": "preco_total",
    "created_at": "data_criacao",
    "updated_at": "data_atualizacao",
    "email": "email_cliente"
}, inplace=True)

# Converter colunas de data para formato datetime
df["data_criacao"] = pd.to_datetime(df["data_criacao"])
df["data_atualizacao"] = pd.to_datetime(df["data_atualizacao"])

# Criar uma nova coluna com o faturamento total por venda
df["total_venda"] = df["quantidade"] * df["preco_unitario"]

# Inserir os dados no MySQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO vendas (
            id_venda, cliente, email_cliente, id_produto, produto, preco_unitario, quantidade,
            preco_total, total_venda, data_criacao, data_atualizacao
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["id_venda"], row["cliente"], row["email_cliente"], row["id_produto"], row["produto"],
        row["preco_unitario"], row["quantidade"], row["preco_total"], row["total_venda"],
        row["data_criacao"], row["data_atualizacao"]
    ))

#confimar e fechar a conexão
conn.commit()
cursor.close()
conn.close()

print("Dados inseridos no MySQL com sucesso!")
