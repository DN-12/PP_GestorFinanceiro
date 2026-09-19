import sqlite3
from datetime import date

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

print("Banco de dados configurado!")

#Funçao que registra uma entrada
def registrar_entrada():
    valor = float(input("Valor: "))
    descricao = str(input("Descrição: "))
    categoria = str(input("Categoria: "))
    data = str(date.today())
    cursor.execute("""INSERT INTO lancamentos (tipo,valor,descricao,categoria,data) VALUES (?,?,?,?,?)""",("entrada", valor,descricao,categoria,data))
    conexao.commit()
    return valor,descricao,categoria,data
#Funçao que registra uma saida
def registrar_saida():
    valor = float(input("Valor: "))
    descricao = str(input("Descrição: "))
    categoria = str(input("Categoria: "))
    data = str(date.today())
    cursor.execute("""INSERT INTO lancamentos (tipo,valor,descricao,categoria,data) VALUES (?,?,?,?,?)""",("saida", valor,descricao,categoria,data))
    conexao.commit()
    return valor,descricao,categoria,data
#Extrato
def listar_lancamentos():
    lista = cursor.execute("""SELECT * FROM lancamentos""").fetchall()
    for dado in lista:
        id = dado[0]
        tipo = dado[1]
        valor = dado[2]
        descricao = dado[3]
        categoria = dado[4]
        data = dado[5]
        print(f"{id} | {tipo} | Valor R${valor} | Desc: {descricao} | Categoria: {categoria} | Data: {data}")
#Calcula todas as entradas
def calcular_entradas():
    entradas = cursor.execute("""SELECT SUM(valor) FROM lancamentos WHERE tipo = 'entrada'""").fetchone()
    return entradas[0]
#Calcula todas as saidas
def calcular_saidas():
    saidas = cursor.execute("""SELECT SUM(valor) FROM lancamentos WHERE tipo = 'saida'""").fetchone()
    return saidas[0]
#Consulta saldo 
def calcular_saldo():
    saldo = cursor.execute("""SELECT SUM(CASE WHEN tipo = 'entrada' THEN valor ELSE 0 END) - SUM(CASE WHEN tipo = 'saida' THEN valor ELSE 0 END) FROM lancamentos""").fetchone()
    return saldo[0]
menu = 0
while menu != 4:
    print("===== Menu =====")
    menu = int(input("1 - Entrada \n2 - Saida \n3 - Extrato \n4 - Sair\n"))
    if menu == 1:
        registrar_entrada()
    elif menu == 2:
        registrar_saida
    elif menu == 3:
        entradas = calcular_entradas()
        saidas = calcular_saidas()
        saldo = calcular_saldo()
        listar_lancamentos()
        print(f"Entradas: R${entradas} | Saidas: R${saidas} | Saldo: R${saldo}")
    elif menu == 4:
        print("Encerrando...")
    else:
        print("Opção inválida!")
    
    





