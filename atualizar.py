import sqlite3

# 1. Conectamos ao nosso banco de dados existente
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

print("--- ANTES DA ATUALIZAÇÃO ---")
# Vamos consultar como está o Plástico Bolha antes de mexer
cursor.execute("SELECT nome, qtd_atual FROM produtos WHERE nome LIKE '%Plástico Bolha%'")
produto_antes = cursor.fetchone()
print(f"Produto: {produto_antes[0]} | Quantidade Atual: {produto_antes[1]}")

# 2. O COMANDO UPDATE: Atualizando o estoque!
# Tradução: "Atualize a tabela produtos, defina a qtd_atual como 25 ONDE o nome seja Plástico Bolha"
cursor.execute('''
    UPDATE produtos 
    SET qtd_atual = 25 
    WHERE nome LIKE '%Plástico Bolha%'
''')

# 3. Salvamos a alteração no banco (o commit do SQLite!)
conexao.commit()

print("\n--- DEPOIS DA ATUALIZAÇÃO ---")
# Consultamos de novo para ver a mágica acontecer
cursor.execute("SELECT nome, qtd_atual, qtd_minima FROM produtos WHERE nome LIKE '%Plástico Bolha%'")
produto_depois = cursor.fetchone()

print(f"Produto: {produto_depois[0]} | Nova Quantidade: {produto_depois[1]} | Mínimo Seguro: {produto_depois[2]}")

if produto_depois[1] >= produto_depois[2]:
    print("✅ Situação normalizada! O estoque está acima do mínimo de segurança.")

# Fechamos a conexão
conexao.close()