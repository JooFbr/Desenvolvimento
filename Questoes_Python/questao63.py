# 63. Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

numeros = []
for i in range(5):
    numero = float(input(f"digite o numero {i + 1}: "))
    numeros.append(numero)
    soma = sum(numeros)
else:
    soma = 0
    print("Nenhum número foi inserido.")

print(f"A soma dos números inseridos é: {soma}")
