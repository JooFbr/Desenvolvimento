# Questão 9 - Escreva um programa que solicite ao usuário um número inteiro e determine se ele é par ou ímpar. Use estruturas condicionais para exibir a mensagem apropriada.

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
