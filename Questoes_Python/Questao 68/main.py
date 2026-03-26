from sistema import SistemaAlunos

sistema = SistemaAlunos()

while True:
    print("""
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Atualizar aluno
5 - Remover aluno
0 - Sair
""")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        nascimento = input("Nascimento (DD/MM/AAAA): ")
        sistema.cadastrar(nome, email, nascimento)

    elif op == "2":
        sistema.listar()

    elif op == "3":
        mat = input("Matrícula: ")
        sistema.exibir(mat)

    elif op == "4":
        mat = input("Matrícula: ")
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        nascimento = input("Nova data: ")
        sistema.atualizar(mat, nome, email, nascimento)

    elif op == "5":
        mat = input("Matrícula: ")
        sistema.remover(mat)

    elif op == "0":
        break

    else:
        print("Opção inválida!")
