import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

cursor.execute("SELECT id, nome, qtd_atual FROM produtos")
todos = cursor.fetchall()

print("--- PRODUTOS CADASTRADOS NO BANCO ---")
for p in todos:
    
    (print(f"ID: {p[0]} | Nome: {p[1]} | Qtd: {p[2]}"))
conexao.close()