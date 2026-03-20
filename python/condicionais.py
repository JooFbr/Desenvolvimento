# aula 3 - Condicional if

# acompanhada = 'Sim'
# idade = 45


# if idade < 0:
#     print("idade invalida")
# elif idade <= 17:
#     print('Voce é menor de idade.')
# else:
#     print('Você é maior de idade')
# if idade >= 18:
#     print('Você pode assistir')
# elif idade < 15:
#     print('Você não pode assistir')
# elif idade <=17:
#     if acompanhada == 'Sim':
#         print('Você pode assistir')
#     else:
#         print('Você não pode assistir')
# else:
#     print('invalido')


# refatorando o codigo

# if idade >= 18:
#     print('Você pode assistir')
# elif (idade >=15 and idade <=17) and acompanhada == 'Sim':
#     print('Você pode assistir')
# else:
#     print('invalido')


print('opção desejada é 0 cadastrar')
print('opção desejada é 1 editar')
print('opção desejada é 2 excluir')


opcao = int(input('O que deseja fazer?'))

match opcao:
    case 0:
        print('voce escolheu cadastrar')
    case 1:
        print('voce escolheu editar')
    case 2:
        print('voce escolheu excluir')
    case _:
        print('Invalido')
