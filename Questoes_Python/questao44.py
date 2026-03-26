# Questao 44: Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

numeros_pares = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
print("Números pares digitados:")
for numero in numeros_pares:
    print(numero)