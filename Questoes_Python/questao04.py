# Questão 4 - Faça um programa que solicite ao usuário escolher uma cor entre "Vermelho", "Azul" e "Verde".
print("Vermelho")
print("Azul")
print("Verde")


cor = str(input("Escolha uma cor:"))


if cor == "Vermelho":
    print("Você escolheu Vermelho!")
elif cor == "Azul":
    print("Você escolheu Azul!")
elif cor == "Verde":
    print("Você escolheu Verde!")
else:
    print("Opção inválida. Por favor escolha uma das opcões.")