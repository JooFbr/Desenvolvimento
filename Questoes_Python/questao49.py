#49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

numeros = []
for i in range(7):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
contador_maiores_que_10 = sum(1 for numero in numeros if numero > 10)
print(f"Quantidade de números maiores que 10: {contador_maiores_que_10}")