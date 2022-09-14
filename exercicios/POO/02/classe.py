class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def listar(self):
        print(f'Nome: {self.__nome}')

class Aluno(Pessoa):
    def __init__(self, nome, ano_nascimento, ano_escolar):
        super().__init__(nome)
        self.__ano_nascimento = ano_nascimento
        self.__ano_escolar = ano_escolar

    def listar_aluno(self):
        super().listar()
        print(f'Idade: {self.idade_aluno()}')
        print(f'Ano: {self.__ano_escolar}')

    def alterar_ano_escolar(self, valor):
        self.__ano_escolar = valor

    def idade_aluno(self):
        return (2022 - self.__ano_nascimento) 

    
class Professor(Pessoa):
    __materias = ['Matemática', 'Português', 'História', 'Química', 'Física', 'Geografia' ]
    def __init__(self, nome, cpf, materia):
        super().__init__(nome) 
        self.__cpf = cpf 
        self.__materia = materia

    def listar_professor(self):
        super().listar()
        print(f'    CPF: {self.__cpf}')
        print(f'MATÉRIA: {self.__materias[self.__materia]}')

