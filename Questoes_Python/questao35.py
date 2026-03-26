#Questao 35: Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

multiplicacao = numero_1 * numero_2
if multiplicacao == 20:
    print("A multiplicação dos dois números é igual a 20.")
else:
    print(f"A multiplicação dos dois números é igual a {multiplicacao}, e não 20.")