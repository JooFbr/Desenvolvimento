# Questao 41: Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.

numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    print(f"Números de 1 até {numero}:")
    for i in range(1, numero + 1):
        print(i)
else:
    print("Por favor, digite um número inteiro positivo.")
    