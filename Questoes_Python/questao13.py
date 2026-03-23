# Questão 13 - Escreva um programa que solicite ao usuário o número do mês (1-12) e exiba a estação do ano correspondente (verão, outono, inverno ou primavera). Use estruturas condicionais para determinar a estação com base no número do mês.

mes = int(input("Digite o número do mês (1-12): "))
if mes == 1 or mes == 2 or mes == 12:
    print("É verão!")
elif mes == 3 or mes == 4 or mes == 5:
    print("É outono!")
elif mes == 6 or mes == 7 or mes == 8:
    print("É inverno!")
else:
    print("Mês inválido.")