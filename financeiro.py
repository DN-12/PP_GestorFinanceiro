from banco import cursor
#Calcula todas as entradas
def calcular_entradas():
    entradas = cursor.execute("""SELECT SUM(valor) FROM lancamentos WHERE tipo = 'entrada'""").fetchone()
    return entradas[0]
#Calcula todas as saidas
def calcular_saidas():
    saidas = cursor.execute("""SELECT SUM(valor) FROM lancamentos WHERE tipo = 'saida'""").fetchone()
    return saidas[0]
#Calcula saldo 
def calcular_saldo():
    saldo = cursor.execute("""SELECT SUM(CASE WHEN tipo = 'entrada' THEN valor ELSE 0 END) - SUM(CASE WHEN tipo = 'saida' THEN valor ELSE 0 END) FROM lancamentos""").fetchone()
    return saldo[0]