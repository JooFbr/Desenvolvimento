# 46. Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print(f"A média dos números inseridos é: {media}")
