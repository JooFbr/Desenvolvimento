# 55. Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

while True:
    numero = int(input("Digite um número que seja maior que 100: "))
    if numero > 100:
        print(f"Obrigado por inserir o número {numero}, que é maior que 100!")
        break
    else:
        print("Número inválido. Por favor, faça direito e insira um número maior que 100!")
