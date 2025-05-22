import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect('serie.db')
cursor = conexao.cursor()

# Inserindo os nossos Dados
cursor.execute(
    """
        INSERT INTO series(nome, ano, nota)
        VALUES ('Suits', 2011, 8.4)
    """

)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela com sucesso!")