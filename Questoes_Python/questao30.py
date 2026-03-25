# 30. Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print(f"Você tem {idade} anos e pode votar.")
else:
    print(f"Você tem {idade} anos e não pode votar.")
