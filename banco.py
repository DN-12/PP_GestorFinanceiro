import sqlite3

conexao = sqlite3.connect("financeiroexemplo.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS lancamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    valor REAL NOT NULL,
    descricao TEXT NOT NULL,
    categoria TEXT NOT NULL,
    data TEXT NOT NULL
)
""")

conexao.commit()
