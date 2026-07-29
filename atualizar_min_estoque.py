import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

print("--- ATUALIZAR ESTOQUE MÍNIMO DE SEGURANÇA ---")
id_produto = input("Digite o ID do produto (1: Caixas | 2: Plástico Bolha | 3: Fita): ")
novo_minimo = input("Digite o novo valor para o ESTOQUE MÍNIMO: ")

# O comando UPDATE alterando especificamente a coluna qtd_minima
cursor.execute("UPDATE produtos SET qtd_minima = ? WHERE id = ?", (novo_minimo, id_produto))
conexao.commit()

print("✅ Estoque mínimo atualizado com sucesso!")
conexao.close()