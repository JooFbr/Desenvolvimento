# 23. Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python".

palavra = str(input("Digite uma palavra: "))

if palavra == "Python":
    print(f"A palavvra digitada é {palavra}!")
else:
    print(f"A palavra digitada não é Python, é {palavra}! Digite Python para ser Alfa.")
