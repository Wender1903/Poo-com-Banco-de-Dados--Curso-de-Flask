import sqlite3

conexao = sqlite3.connect('serie.db')
cursor = conexao.cursor()

# Atualizando dados 
id = 2
cursor.execute(
    """
        UPDATE series SET nota = ?
        WHERE id = ?
    """,

    (8.8, id)
)
conexao.commit()
print(f"Dados da serie {id}, atualizados com sucesso!!")