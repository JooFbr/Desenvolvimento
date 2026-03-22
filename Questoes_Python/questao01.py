# Questão 1 - Faça um programa que apresente um menu de opções para o usuário escolher um número entre 1 e 3.
 
import os

print("Número 1")
print("Número 2")
print("Número 3")

opcao = int(input("Escolha um número: "))

os.system("cls")

match opcao:
    case 1:
        print("Você escolheu o número Um ;)")
    case 2:
        print("você escolheu o número Dois =>")
    case 3:
        print("Você escolheu o número Três =)")
    case _:
        print("Opção inválida. Por favor escolha um número entre 1 e 3.")