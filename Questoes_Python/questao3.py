# Questão 3 - Faça um programa que solicite um número ao usuário e informe o dia da semana correspondente 
# (1 para Domingo, 2 para Segunda, etc.). Utilize a estrutura match-case para resolver o problema.

dia = int(input("Escolha um número de 1 a 7: "))


match dia:
    case 1:
        print("Você escolheu Domingo!")
    case 2:
        print("Você escolheu Segunda!")
    case 3:
        print("Você escolheu Terça!")
    case 4:
        print("Você escolheu Quarta!")
    case 5:
        print("Você escolheu Quinta!")
    case 6:
        print("Você escolheu Sexta!")
    case 7:
        print("Você escolheu Sábado!")
    case _:
        print("Opção inválida. Por favor escolha um número entre 1 e 7.")
