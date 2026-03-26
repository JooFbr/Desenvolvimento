#questao 36: Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

numero_mes = int(input("Digite um número de 1 a 12 para saber o mês correspondente: "))

if numero_mes == 1:
    print("O mês correspondente é Janeiro.")    
elif numero_mes == 2:
    print("O mês correspondente é Fevereiro.")
elif numero_mes == 3:
    print("O mês correspondente é Março.")
elif numero_mes == 4:
    print("O mês correspondente é Abril.")
elif numero_mes == 5:
    print("O mês correspondente é Maio.")
elif numero_mes == 6:
    print("O mês correspondente é Junho.")
elif numero_mes == 7:
    print("O mês correspondente é Julho.")
elif numero_mes == 8:
    print("O mês correspondente é Agosto.")
elif numero_mes == 9:
    print("O mês correspondente é Setembro.")
elif numero_mes == 10:
    print("O mês correspondente é Outubro.")
elif numero_mes == 11:
    print("O mês correspondente é Novembro.")
elif numero_mes == 12:
    print("O mês correspondente é Dezembro.")
else:
    print("Número inválido. Digite um número de 1 a 12.")