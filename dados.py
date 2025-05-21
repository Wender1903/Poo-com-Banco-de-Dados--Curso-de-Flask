import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect('serie.db')
cursor = conexao.cursor()

# Inserindo os nossos Dados
cursor.execute(
    """
        INSERT INTO series(nome, ano, nota)
        VALUES ('Tudo Bem Não Ser Normal', 2020, 8.6)
    """

)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela com sucesso!")