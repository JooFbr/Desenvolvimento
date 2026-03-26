# 54. Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    if numero < 0:
        print("Número negativo inserido. Encerrando o programa.")
        break
    else:
        print(f"Você digitou: {numero}. Digite outro número ou um número negativo para sair.")