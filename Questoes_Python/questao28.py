# 28. Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

palavra = str(input("Digite uma palavra: "))

if len(palavra) > 5:
    print(f"A palavra '{palavra}' tem mais de 5 letras.")
else:
    print(f"A palavra '{palavra}' não tem mais de 5 letras.")