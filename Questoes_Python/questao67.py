# 67. desenvolva um jogo da velha em python que funcione no terminal.

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
        [0,1,2], [3,4,5], [6,7,8],  # linhas
        [0,3,6], [1,4,7], [2,5,8],  # colunas
        [0,4,8], [2,4,6]            # diagonais
    ]
    
    for combo in combinacoes:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == jogador:
            return True
    return False


def jogo_da_velha():
    tabuleiro = [" "]*9
    jogador_atual = "X"

    for rodada in range(9):
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

            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu! Parabéns seu coco!")
                return

            # troca de jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"

        except ValueError:
            print("Digite um número válido!")

    mostrar_tabuleiro(tabuleiro)
    print("Deu empate!")

jogo_da_velha()