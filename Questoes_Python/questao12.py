# Questão 12 - Escreva um programa que solicite ao usuário o meio de transporte que ele usa (carro, bicicleta, ônibus, trem, a pé) e exiba a velocidade média correspondente a esse meio de transporte.

transporte = input("Digite o meio de transporte que você usa: (carro, bicicleta, ônibus, trem, a pé) ")
if transporte == "carro":
    print("Velocidade média: 60 km/h")
elif transporte == "bicicleta":
    print("Velocidade média: 15 km/h")
elif transporte == "ônibus":
    print("Velocidade média: 40 km/h")
elif transporte == "trem":
    print("Velocidade média: 80 km/h")
elif transporte == "a pé":
    print("Velocidade média: 5 km/h")
else:
    print("Meio de transporte desconhecido.")
