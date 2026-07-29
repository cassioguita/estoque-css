import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Pedimos para você digitar no terminal qual produto quer mexer e a nova quantidade
nome_produto = input("Digite o nome (ou parte do nome) do produto que deseja atualizar: ")
nova_qtd = int(input("Digite a nova quantidade atual: "))

# Atualiza no banco usando o que você digitou
cursor.execute('''
    UPDATE produtos 
    SET qtd_atual = ? 
    WHERE nome LIKE ?
''', (nova_qtd, f'%{nome_produto}%'))

conexao.commit()

print(f"\n✅ Estoque atualizado com sucesso para '{nome_produto}'!")
conexao.close()