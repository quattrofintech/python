from random import randint


class Pessoa:
    def __init__(self, nome, nascimento):
        self.__codigo = self.__gerarCodigo()
        self.__nome = nome
        self.__nascimento = nascimento
        

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def nascimento(self):
        return self.__nascimento

    @staticmethod
    def __gerarCodigo():
        return randint(10000, 99999)

    def exibirPessoa(self):
        print(f'Codigo: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'Nascimento: {self.nascimento}')

class Funcionario(Pessoa):
    def __init__(self, nome, nascimento, veiculo):
        super().__init__(nome, nascimento)
        self.__matricula = self.__gerarMatricula()
        self.__veiculo = veiculo 
        self.__dependentes = []

    @property
    def matricula(self):
        return self.__matricula

    @property
    def veiculo(self):
        return self.__veiculo.exibirVeiculo()
    
    @property
    def dependentes(self):
        for dep in self.__dependentes:
            print('---' * 10)
            print(f' - Codigo: {dep.codigo}')
            print(f' - Nome: {dep.nome}')
            print(f' - Nascimento: {dep.nascimento}')
            print(f' - Parentesco: {dep.parentesco}')

    @staticmethod
    def __gerarMatricula():
        return randint(100000, 999999)

    def addDepend(self, nome, nascimento, parentesco):
        dep = Dependente(nome, nascimento, self.nome, parentesco)
        self.__dependentes.append(dep)

    def exibirFuncionario(self):
        super().exibirPessoa()
        print(f'Matricula: {self.matricula}')
        print(f'Dependentes')
        self.dependentes
        print(f'Veiculo')
        self.veiculo

class Dependente(Pessoa):
    def __init__(self, nome, nascimento, funcionario, parentesco):
        super().__init__(nome, nascimento)
        self.__funcionario = funcionario
        self.__parentesco = parentesco
    
    @property
    def funcionario(self):
        return self.__funcionario
    
    @property
    def parentesco(self):
        return self.__parentesco

    
    def exibirDependente(self):
        super().exibirPessoa()
        print(f'Parentesco: {self.parentesco}')


class Veiculo:
    def __init__(self, modelo, placa):
        self.__codigo = self.__gerarCodigo()
        self.__modelo = modelo
        self.__placa = placa

    @property
    def codigo(self):
        return self.__codigo

    @property
    def modelo(self):
        return self.__modelo

    @property
    def placa(self):
        return self.__placa

    @staticmethod
    def __gerarCodigo():
        return randint(10, 99)

    def exibirVeiculo(self):
        print(f' - Codigo: {self.codigo}')
        print(f' - Modelo: {self.modelo}')
        print(f' - Placa: {self.placa}')