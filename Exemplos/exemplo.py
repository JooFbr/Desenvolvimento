import os
from funcoes import soma, sub, menu

continuar = 's'
while continuar != 'n':
    os.system('cls')
    opcao = menu()

    numero1 = int(input("informe primeiro numero: "))
    numero2 = int(input("informe segundo numero: "))

    if opcao == '1':
        soma(numero1, numero2)
    elif opcao == '2':
        sub(numero1, numero2)
    else:
        print('Opção Invalida')

    continuar = input('Deseja realizar outra soma s/n?')
