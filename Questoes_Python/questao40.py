# Questao 40: Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))
if numero_1 == numero_2 == numero_3:
    print("Todos os números são iguais.")
else:
    print("Os números não são todos iguais.")
    