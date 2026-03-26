import uuid

class Aluno:
    def __init__(self, nome, email, nascimento):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento
        self.matricula = self.gerar_matricula()

    def gerar_matricula(self):
        return str(uuid.uuid4())[:8]  # matrícula única curta

    def __str__(self):
        return (
            f"Matrícula: {self.matricula}\n"
            f"Nome: {self.nome}\n"
            f"E-mail: {self.email}\n"
            f"Nascimento: {self.nascimento}\n"
        )
    