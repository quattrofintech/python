class Empregado:
    def __init__(self):
        self.__nome = ''
        self.__endereco = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if len(valor) > 10:
            self.__nome = valor.lstrip() # Tirar os espaços em branco do inicio e do final
            return print('Nome Alterado com Sucesso!')
        return print('Nome inválido! Escreva um valor válido!')

    @property
    def endereco(self):
        return self.__endereco 

    @endereco.setter
    def endereco(self, valor):
        self.__endereco = valor

    def adicionarEmpregado(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def exibirEmpregado(self):
        print(f'Nome    : {self.nome}')
        print(f'Endereco: {self.endereco}')

class Chefe(Empregado):
    def __init__(self):
        super().__init__()
        self.__salarioMensal = 0

    @property
    def salario(self):
        return self.__salarioMensal

    @salario.setter
    def salario(self, valor):
        if float(valor):
            self.__salarioMensal += round(float(valor), 2)
        else:
            print('Insira valores financeiros válidos!')

    def adicionarSalario(self, valor):
        self.salario = valor

    def calcularSalario(self):
        print(f'Salário: R$ {self.salario}')

class Comissionado(Empregado):
    def __init__(self, salario, comissao, quantidade):
        super().__init__()
        self.__salarioBase = salario
        self.__comissao = comissao
        self.__quantidade = quantidade

    @property
    def salarioBase(self):
        return self.__salarioBase

    @property
    def comissao(self):
        return self.__comissao

    @property
    def quantidade(self):
        return self.__quantidade


    def calcularSalario(self):
        salario = self.salarioBase + ( self.comissao * self.quantidade)
        return float(salario)




