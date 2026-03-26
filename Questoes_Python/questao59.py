# 59. Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 > num2:
        print(f"{num1} é maior que {num2}.")
        break
    else:
        print(f"{num1} não é maior que {num2}. Tente novamente.")
        