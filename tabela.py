import sqlite3

# Conectando com o BD
conexao = sqlite3.connect('serie.db')

# Criando cursor
cursor = conexao.cursor()

# Criando a tabela
cursor.execute(
    """
        CREATE TABLE series(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# Fecha conexão
conexao.close()
print("A tabela foi Criada com Sucesso!")