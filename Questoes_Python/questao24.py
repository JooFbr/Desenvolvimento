# 24. Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.

cidade = str(input("Digite o nome de uma cidade: "))

if cidade == "Brasília":
    print(f"{cidade} é a capital do Brasil!")
elif cidade:
    print(f"{cidade} não é a capital do Brasil, a capital do Brasil é Brasília!")
else:
    print("Nenhuma cidade foi digitada, por favor digite uma cidade para verificar se é a capital do Brasil.")
