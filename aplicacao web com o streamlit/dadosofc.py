import sqlite3

# Função para conectar-se ao Banco de Dados
def conecta_bd():
    conexao = sqlite3.connect('serie.db')
    return conexao

# Inserir Dados
def inserir_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    
    cursor.execute(
        f"""
            INSERT INTO series(nome, ano, nota)
            VALUES(?, ?, ?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()

# Listar Dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    dados = cursor.execute("SELECT * FROM series")
    return dados.fetchall()