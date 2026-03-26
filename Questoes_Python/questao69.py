# Questão 69 - Versão melhorada do jogo da velha

def mostrar_tabuleiro(tab):
    print()
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    print()


def verificar_vitoria(tab, jogador):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    return any(tab[a] == tab[b] == tab[c] == jogador for a,b,c in combinacoes)


def jogo():
    tabuleiro = [" "] * 9
    jogador_atual = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)

        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1

            if jogada < 0 or jogada > 8:
                print("Posição inválida!")
                continue

            if tabuleiro[jogada] != " ":
                print("Essa posição já está ocupada!")
                continue

            tabuleiro[jogada] = jogador_atual

            # verifica vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break

            # verifica empate
            if " " not in tabuleiro:
                mostrar_tabuleiro(tabuleiro)
                print("Deu empate!")
                break

            # troca jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"

        except ValueError:
            print("Digite um número válido!")


def jogo_da_velha():
    while True:
        jogo()

        opcao = input("Deseja jogar novamente? (s/n): ").lower()
        if opcao != "s":
            print("Obrigado por jogar!")
            break

jogo_da_velha()