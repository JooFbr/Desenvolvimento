# 62. Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

nomes = []
for i in range(3): 
    nome = str(input(f"Digite o nome {i + 1}: "))
    nomes.append(nome)
print("Os nomes inseridos são:", nomes)
