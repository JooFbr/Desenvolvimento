# 60. Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

numero1 = int(input("Digite um número: "))
divisores = []

for i  in range(1, numero1 + 1):
    if numero1 % i == 0: 
        divisores.append(i)
        print(f"{i} é um divisor de {numero1}.")
        print(f"Os divisores de {numero1} são: {divisores}.")
    else:
        print(f"{i} não é um divisor de {numero1}.")
