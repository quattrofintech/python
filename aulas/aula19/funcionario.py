class Funcionario:
    __valor_hora_cargo = [189.56,      86.05,      35.48]
    __nome_cargo =       ['Diretor', 'Gerente', 'Vendedor'] # 0 - 1 - 2 

    def __init__(self, nome, cargo, horas_trabalhadas):
        self.nome = nome
        self.cargo = cargo
        self.horas_trabalhadas = horas_trabalhadas
        self.__salario = 0

    def exibir_funcionario(self):
        print(f'NOME: {self.nome}')
        print(f'CARGO: {self.cargo} - {self.__nome_cargo[self.cargo]}')
        print(f'HORAS TRABALHADAS: {self.horas_trabalhadas} horas')
        print(f'SALÁRIO: R$ {self.__salario}')

    def adicionar_horas_trabalhadas(self):
        self.horas_trabalhadas += 1

    def calcular_salario(self):
        self.__salario = self.horas_trabalhadas * self.__valor_hora_cargo[self.cargo]

    @classmethod
    def alterar_salario_funcionarios(cls, indice, valor):
        cls.__valor_hora_cargo[indice] = valor

    @classmethod # decorador
    def retornar_cargos(cls):
        return cls.nome_cargo


fun = Funcionario('Gabriel', 0, 10)
# fun.__valor_hora_cargo =  [1250]
# fun._Funcionario__valor_hora_cargo[0] = 545
fun.calcular_salario()
fun.__salario = 5000
print(fun.exibir_funcionario())




