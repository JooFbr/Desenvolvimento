mes = int(input("Digite o número do mês (1-12): "))
if mes == 1 or mes == 2 or mes == 12:
    print("É verão!")
elif mes == 3 or mes == 4 or mes == 5:
    print("É outono!")
elif mes == 6 or mes == 7 or mes == 8:
    print("É inverno!")
else:
    print("Mês inválido.")