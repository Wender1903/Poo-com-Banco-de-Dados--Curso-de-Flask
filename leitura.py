import sqlite3

# Conectando ao Banco de Dados
conexao = sqlite3.connect('serie.db')
cursor = conexao.cursor()

# Leitura dos dados

dados = cursor.execute("SELECT * FROM series")
print(dados.fetchall())