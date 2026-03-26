# 66. Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

import sys

cadastros = []
while True:
    print("\nMenu:")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Exccluir nome")
    print("4 - Listar todos os cadastrados")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome para cadastrar: ")
        cadastros.append(nome)
        print(f"Nome '{nome}' cadastrado com sucesso.")

    elif opcao == "2":
        nome_atual = input("Digite o novo nome para atualizar: ")
        if nome_atual in cadastros:
            novo_nome = input("Digite o novo nome: ")
            cadastros[cadastros.index(nome_atual)] = novo_nome
            print(
                f"Nome '{nome_atual}' atualizado para '{novo_nome}' com sucesso.")
        else:
            print(f"Nome '{nome_atual}' não encontrado para atualização.")

    elif opcao == "3":
        nome_excluir = input("Digite o seu nome para poder excluir: ")
        if nome_excluir in cadastros:
            cadastros.remove(nome_excluir)
            print(f"{nome_excluir} foi apagado da existencia.")
        else:
            print(
                f"Nome '{nome_excluir}' não foi encontrado para a exclusão. Verifique se o nome está correto.")

    elif opcao == "4":
        if cadastros:
            print("Nomes cadastrados no system:")
            for nome in cadastros:
                print(nome)
        else:
            print("Nenhum nome cadastrado.")

    elif opcao == "5":
        print("Encerrando o system. Até mais!")
        sys.exit()
    else:
        print("Opção inválida. Seleciona uma opção válida.")

    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != "s":
        print("Encerrando o system. Até mais!")
        break
