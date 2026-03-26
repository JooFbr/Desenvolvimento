from aluno import Aluno
from utils import validar_nome, validar_email, validar_data

class SistemaAlunos:
    def __init__(self):
        self.alunos = []

    def cadastrar(self, nome, email, nascimento):
        if not validar_nome(nome):
            print("Nome inválido!")
            return

        if not validar_email(email):
            print("Email inválido!")
            return

        if not validar_data(nascimento):
            print("Data inválida! Use DD/MM/AAAA")
            return

        aluno = Aluno(nome, email, nascimento)
        self.alunos.append(aluno)
        print(f"Aluno cadastrado! Matrícula: {aluno.matricula}")

    def buscar(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def listar(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return

        for aluno in self.alunos:
            print("="*30)
            print(aluno)

    def exibir(self, matricula):
        aluno = self.buscar(matricula)
        if aluno:
            print(aluno)
        else:
            print("Matrícula não encontrada!")

    def atualizar(self, matricula, nome, email, nascimento):
        aluno = self.buscar(matricula)

        if not aluno:
            print("Matrícula inválida!")
            return

        if validar_nome(nome):
            aluno.nome = nome

        if validar_email(email):
            aluno.email = email

        if validar_data(nascimento):
            aluno.nascimento = nascimento

        print("Dados atualizados!")

    def remover(self, matricula):
        aluno = self.buscar(matricula)

        if aluno:
            self.alunos.remove(aluno)
            print("Aluno removido!")
        else:
            print("Matrícula inválida!")