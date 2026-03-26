# Questao 34: Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
