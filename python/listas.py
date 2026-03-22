# lista 

# nome = 'Davi'

# print(f'meu nome é {nome}')

# nomes = ['Davi','João','Marcelo']

# print(nomes[0])
# print(nomes[1])


# Percorrendo a lista posição por posição

apostolos = ['Tiago','Mateus','Pedro','Lucas','Judas']

# # for apostolo in apostolos:
# #     print(apostolo)

# #adicionando itens na lista

# print(apostolos)
# apostolos.append('João')
# print(apostolos)


# #adicionando em posição desejada
# apostolos.insert(2,'Simão')
# print(apostolos)


#exapandindo a listas com novos elementos

cavaleiros = ['Seiya', 'Shiryu']
print(cavaleiros)

cavaleiros.extend(['Ikki', 'Yoga', 'Shun'])
print(cavaleiros)



# excluindo itens de uma lista

# cavaleiros.pop()
# print(cavaleiros)


# cavaleiros.pop(0)
# print(cavaleiros)


# excluindo por valor

# print(apostolos)
# apostolos.remove('Judas')
# print(apostolos)


# alunos = ['Victor', 'Lucas', 'Gabriel', 'Lucas', 'Amanda', 'Daniel']
# print(alunos)

# alunos.remove('Lucas')
# print(alunos)

# for indice ,aluno in enumerate(alunos):
#     if aluno == 'Lucas':
#         alunos.pop(aluno)

# print(alunos)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []
pares = []

for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)
    elif numero % 2 == 0:
        pares.append(numero)

print(impares)
print(pares)


print(apostolos)
apostolos.sort()
print(apostolos)
apostolos.reverse()
print(apostolos)


print(cavaleiros)
cavaleiros.clear()
print(cavaleiros)


print(pares)
del pares
print(pares)