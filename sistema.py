import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# 1. Cria a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        qtd_atual INTEGER,
        qtd_minima INTEGER
    )
''')

# 2. Insere os produtos
cursor.execute("INSERT INTO produtos (nome, qtd_atual, qtd_minima) VALUES ('Caixas de Papelão', 500, 100)")
cursor.execute("INSERT INTO produtos (nome, qtd_atual, qtd_minima) VALUES ('Plástico Bolha (Rolos)', 5, 10)")
cursor.execute("INSERT INTO produtos (nome, qtd_atual, qtd_minima) VALUES ('Fita Adesiva', 20, 50)")

conexao.commit()
conexao.close()

print("Banco de dados criado e produtos cadastrados com sucesso!")