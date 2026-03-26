#Questao 33: Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10% para compras acima de R$ 100,00.

valor_produto = float(input("Digite o valor do produto: R$ "))

if valor_produto > 100:
    desconto = valor_produto * 0.10
    valor_com_desconto = valor_produto - desconto
    print(f"O valor do produto com desconto é: R$ {valor_com_desconto:.2f}")
else:
    print(f"O valor do produto é: R$ {valor_produto:.2f} (sem desconto)")