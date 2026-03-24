# Questao 20: Crie um programa que solicite ao usuário a temperatura em graus Celsius e converta para Fahrenheit.

celsius = float(input("Digite aqui a temperatura em grau celsius: "))

fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")