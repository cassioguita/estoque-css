import sqlite3

# 1. Conectamos ao banco de dados que já existe
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# 2. Fazemos a pergunta ao banco (O nosso SELECT)
cursor.execute('SELECT nome, qtd_atual, qtd_minima FROM produtos WHERE qtd_atual < qtd_minima')

# 3. Guardamos a resposta em uma variável
produtos_em_falta = cursor.fetchall()

print("--- RELATÓRIO DE REPOSIÇÃO DE ESTOQUE ---")

# 4. A lógica: se a lista estiver vazia, tá tudo ok. Se tiver algo, ele alerta!
if len(produtos_em_falta) == 0:
    print("✅ Tudo certo! Nenhum produto precisa de reposição no momento.")
else:
    for produto in produtos_em_falta:
        nome = produto[0]
        atual = produto[1]
        minima = produto[2]
        
        print(f"⚠️ ALERTA: {nome} | Estoque Atual: {atual} | Mínimo Seguro: {minima}")

# Fechamos a conexão
conexao.close()