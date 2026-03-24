# Questao 17: Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.

numero_1 = float(input("Informe numero: "))
numero_2 = float(input("Informe o segundo numero: "))

soma = numero_1 + numero_2
sub = numero_1 - numero_2
div = numero_1 / numero_2
mult = numero_1 * numero_2

print(f'Resultado da soma: {soma:.2f}')
print(f'Resultado da subtração: {sub:.2f}')
print(f'Resultado da divisão: {div:.2f}')
print(f'Resultado da multiplicação: {mult:.2f}')
