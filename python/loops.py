# WHILE

# cont = 0

# while True:
#     cont = cont + 1
#     print(cont)
#     if cont >= 100:
#         break

# sair = "não"
# while "sair" != "sim":
#     print ("0 - Cadastrar")
#     print ("1 - Editar")
#     print ("2 - Excluir")

#     opcao = int(input("O que deseja fazer? "))

#     match opcao:
#         case 0:
#             print("Cadastrando...")
#             sair = input('Deseja sair? (sim/não): ')
#         case 1:
#             print("Editando...")
#             sair = input('Deseja sair? (sim/não): ')
#         case 2:
#             print("Excluindo...")
#             sair = input('Deseja sair? (sim/não): ')
#         case _:
#             print("Opção inválida. Tente novamente.")

# FOR para Repetição pre definido de vezes


# for numero in range(1,11):
#     print(numero)

# percorrendo Listas

# frutas = ['Uva','Maça', 'Melão', 'Kiwi']

# for fruta in frutas:
#     print(fruta)


nome = 'João'

for letra in nome:
    print(letra)
