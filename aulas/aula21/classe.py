from random import randint
class Cliente:
    #dunder
    def __init__(self, nome, sexo, telefone, endereco):
        # Inicializar os Atributos
        self.__codigo = self.gerar_codigo_usuario()
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.endereco = endereco

    @classmethod
    def gerar_codigo_usuario(cls):
        return randint(100000, 999999)

    def atualizar_endereco(self, valor):
        self.endereco = valor

    def atualizar_telefone(self, valor):
        self.telefone = valor

    def listar_cliente(self):
        print(f'Codigo: {self.__codigo}')
        print(f'Nome: {self.nome}')
        print(f'Sexo: {self.sexo}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')


class Funcionario:
    def __init__(self, nome, sexo, telefone, endereco, horasTrabalhadas):
        self.__codigo = self.gerar_codigo_funcionario()
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.endereco = endereco
        self.horas_trabalhadas = horasTrabalhadas
        self.__salario = 0

    @staticmethod
    def gerar_codigo_funcionario():
        return randint(10000, 99999)

    def atualizar_endereco(self, valor):
        self.endereco = valor

    def atualizar_telefone(self, valor):
        self.telefone = valor

    def listar_funcionario(self):
        print(f'Codigo: {self.__codigo}')
        print(f'Nome: {self.nome}')
        print(f'Sexo: {self.sexo}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
        print(f'Horas: {self.horas_trabalhadas}')
        print(f'Salário: R$ {self.__salario}')

    def adicionar_horas_trabalhadas(self, valor):
        self.horas_trabalhadas += valor

    def calcular_salario(self):
        self.__salario = self.horas_trabalhadas * 34.89
    


class Animal:
    __animal  = ['Cachorro', 'Gato', 'Tartaruga', 'Pássaro', 'Peixe']
    def __init__(self, nome, sexo, animal, peso):
        self.__codigo = self.gerar_codigo_animal()
        self.nome = nome
        self.sexo = sexo
        self.animal = animal
        self.peso = peso

    @staticmethod
    def gerar_codigo_animal():
        return randint(1, 1000)

    def adicionar_peso(self, valor):
        self.peso += valor
    
    def listar_animal(self):
        print(f'Codigo: {self.__codigo}')
        print(f'  Nome: {self.nome}')
        print(f'  Sexo: {self.sexo}')
        print(f'  Tipo: {self.__animal[self.animal]}')
        print(f'  Peso: {self.peso}')
