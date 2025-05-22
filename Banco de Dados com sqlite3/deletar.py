import sqlite3

conexao = sqlite3.connect('serie.db')
cursor = conexao.cursor()

# Deletar Dados
id = (4, 5)
cursor.execute(
    """
        DELETE FROM series
        WHERE ID in (? , ?)
    """,
    id
)
conexao.commit()
print(f"Dados Deletados com Sucesso!!")