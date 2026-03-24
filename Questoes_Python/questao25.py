# 25. Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

numero = int(input("Digite um  número de 0 a 20: "))

if 10 <= numero <= 15:
    print(f"O {numero} está entre 10 e 15.")
else:
    print(f"O {numero} não está entre 10 e 15.")
