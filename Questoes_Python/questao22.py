# 22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if numero_1 > numero_2:
    print(f"{numero_1} é maior que {numero_2}.")
elif numero_1 < numero_2: 
    print(f"{numero_1} é menor que {numero_2}.")