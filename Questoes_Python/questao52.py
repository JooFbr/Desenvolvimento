# 52. Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

senha_correta = "1234"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta. Você nunca vai descobrir essa senha~")