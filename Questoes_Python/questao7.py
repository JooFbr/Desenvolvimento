# Questão 7 - Escreva um programa que solicite ao usuário a nota de um aluno e exiba uma mensagem indicando se a nota é baixa (menor que 5), média (entre 5 e 7) ou alta (maior ou igual a 7). Use estruturas condicionais para determinar a mensagem apropriada.
nota = float(input("Digite a nota do aluno: "))

if nota < 5:
    print("Nota baixa. O aluno está reprovado.")
elif nota >= 5 and nota < 7:
    print("Nota médiana. O aluno está aprovado, mas pode melhorar.")
elif nota >= 7 and nota <= 10:
    print("Nota alta, parabéns! O aluno está aprovado.")
