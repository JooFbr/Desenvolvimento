# Questão 6 - Crie um programa que solicite ao usuário uma operação matemática (soma, subtração, multiplicação ou divisão) e dois números. O programa deve realizar a operação escolhida com os números fornecidos e exibir o resultado. Certifique-se de lidar com casos de divisão por zero.
operacao = input(
    "Digite a operação desejada (soma, subtração, multiplicação ou divisão): ")

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
if operacao == "soma":
    resultado = numero_1 + numero_2
elif operacao == "subtração":
    resultado = numero_1 - numero_2
elif operacao == "multiplicação":
    resultado = numero_1 * numero_2
elif operacao == "divisão":
    if numero_2 != 0:
        resultado = numero_1 / numero_2
    else:
        print("Divisão por zero não é permitida.")
print(f"O resultado é: {resultado}")
