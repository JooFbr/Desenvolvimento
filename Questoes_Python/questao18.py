# Questao 18: Faça um programa que peça ao usuário três números e verifique se todos são positivos.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 >= 0 and numero2 >= 0 and numero3 >= 0:
    print("Todos os numeros são positivos!")
elif numero1 <= 0 and numero2 <= 0 and numero3 <= 0:
    print("Todos os numeros são negativos!")
else:
    print("Um dos numeros não é positivo.")