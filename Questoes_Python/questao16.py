# Questão 16 - Escreva um programa que solicite ao usuário o tipo de combustível (Gasolina, Etanol ou Diesel) e exiba o preço por litro correspondente. Use estruturas condicionais para determinar o preço com base no tipo de combustível escolhido.

combustivel = input("Digite o tipo de combustível que você deseja (Gasolina, Etanol ou Diesel): ")

gasolina = 5.00
etanol = 3.50
diesel = 4.00

if combustivel == "Gasolina":
    print(f"O preço da gasolina é R${gasolina} por litro.")
elif combustivel == "Etanol":
    print(f"O preço do etanol é R${etanol} por litro.")
elif combustivel == "Diesel":
    print(f"O preço do diesel é R${diesel} por litro.")
else:
    print("Tipo de combustível inválido.")