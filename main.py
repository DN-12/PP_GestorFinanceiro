import lancamentos
import financeiro

menu = 0
while menu != 4:
    print("===== Menu =====")
    menu = int(input("1 - Entrada \n2 - Saida \n3 - Extrato \n4 - Sair\n"))
    if menu == 1:
        lancamentos.registrar_entrada()
    elif menu == 2:
        lancamentos.registrar_saida()
    elif menu == 3:
        entradas = financeiro.calcular_entradas()
        saidas = financeiro.calcular_saidas()
        saldo = financeiro.calcular_saldo()
        lancamentos.listar_lancamentos()
        print(f"Entradas: R${entradas} | Saidas: R${saidas} | Saldo: R${saldo}")
    elif menu == 4:
        print("Encerrando...")
    else:
        print("Opção inválida!")
    
    





