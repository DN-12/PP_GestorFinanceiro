from banco import cursor,conexao
from datetime import date

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