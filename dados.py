import sqlite3

#função para conectar
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao


# função para inserir
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO filmes(nome, ano, nota)
            VALUES (?, ?, ?)
        """, (nome, ano, nota)
    )
    conexao.commit()
    conexao.close()

# função para listagem
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados
