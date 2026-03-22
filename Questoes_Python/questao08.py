# Questão 8 - Escreva um programa que solicite ao usuário o estado civil e exiba uma mensagem personalizada para cada estado civil (solteiro, casado, divorciado, viúvo). Use estruturas condicionais para determinar a mensagem apropriada.
estado = input(
    "Digite o seu estado cívil (solteiro, casado, divorciado ou viúvo): ")

if estado == "solteiro":
    print("O que um bonitão como você está fazendo solteiro?")
if estado == "casado":
    print("Parabéns pelo seu casamento!")
if estado == "divorciado":
    print("Pobrezinho, deve estar falido depois do chifre.")
if estado == "víuvo" or estado == "viuvo":
    print("Sinto muito pela sua perda.")
