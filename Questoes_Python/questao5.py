# Questão 5 - Escreva um programa que solicite ao usuário dois números e verifique se ambos são pares. Se ambos os números forem pares, exiba uma mensagem indicando isso; caso contrário, informe que pelo menos um dos números é ímpar.
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))

numero_1 % 2
if numero_1 % 2 == 0 and numero_2 % 2 == 0:
    print("Ambos os números são pares!")
else:
    print("Pelo menos um dos números é ímpar!")
