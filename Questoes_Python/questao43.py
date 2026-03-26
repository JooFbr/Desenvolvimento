# Questao 43: Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

mensagem = input("Digite a mensagem que deseja exibir: ")
repeticoes = int(input("Quantas vezes deseja que a mensagem seja exibida? "))

for i in range(repeticoes):
    print(mensagem)
