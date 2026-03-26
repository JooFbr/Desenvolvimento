# 29. Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.

numero = int(input("Digite um numero: "))

if numero % 3 == 0:
    print(f"O numero {numero} é múltiplo de 3.")
else:
    print(f"O numero {numero} não é múltiplo de 3.")
    