# 53. Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

numero = int(input("Contador regressivo para bombas. Digite um número para começarmos a contagem: "))
while numero >= 1:
    print(numero)
    numero -= 1
print("Bum! A bomba explodiu e você morreu por não correr!")
