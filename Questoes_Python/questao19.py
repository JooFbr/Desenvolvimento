# Questao 19: Escreva um algoritmo que peça ao usuário o nome de uma fruta e verifique se a fruta é uma maçã.

fruta = str(input("Digite aqui sua fruta favorita: ")).lower()

print(f"Sua fruta favorita é: {fruta}")
if fruta == "maçã":
    print(f"Sua fruta é uma {fruta}!!!")
else:
    print(
        f"Sua fruta não é uma maça, é uma {fruta}! Infelismente, você não é chad o suficiente para gostar de maçã.")
