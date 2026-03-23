# Questão 15 - Escreva um programa que solicite ao usuário a idade e exiba uma mensagem indicando se a pessoa é criança (0-12 anos), adolescente (13-17 anos) ou adulta (18 anos ou mais). Use estruturas condicionais para determinar a categoria com base na idade fornecida.

idade = int(input("Digite a sua idade: "))

if idade >= 13 and idade <= 17:
    print("Você é um adolescente!")
elif idade >= 18:
    print("Você é grande!")
else:
    print("Você é criança!")
