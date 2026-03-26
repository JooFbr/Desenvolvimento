# Questao 42: Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.Questao 42: Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

soma = 0
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    soma += numero
print(f"A soma dos números digitados é: {soma}")
    