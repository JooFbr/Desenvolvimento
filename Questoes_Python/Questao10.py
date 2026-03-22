# Questão 10 - Escreva um programa que solicite ao usuário a idade de uma pessoa e determine se ela é maior de idade (18 anos ou mais) ou menor de idade (menos de 18 anos). 

idade = int(input("Digite a idade da pessoa: "))
if idade >= 18: 
    print("Você é maior de idade.")
else: 
    print("Você é menor de idade.")