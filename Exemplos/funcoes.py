def soma(numero1, numero2):
    """
    Esta função recebe dois numeros inteiros e realiza a soma dos mesmos 

    """
    soma = numero1 + numero2
    print(f'O resultado é {soma}')


def sub(numero1, numero2):
    """
    Esta função recebe dois numeros inteiros e realiza a subtração dos mesmos 

    """
    sub = numero1 - numero2
    print(f'O resultado é {sub}')


def menu():
    print('1 - Somar')
    print('2 - Subtrair')
    opcao = input('O que Deseja realizar? ')
    return opcao
