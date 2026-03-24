# 26. Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))

if numero_1 % 5 == 0 and numero_2 % 5 == 0:
    print(f"Os números {numero_1} e {numero_2} são múltiplos de 5.")
else:
    print(f"Os números {numero_1} e {numero_2} não são múltiplos de 5.")