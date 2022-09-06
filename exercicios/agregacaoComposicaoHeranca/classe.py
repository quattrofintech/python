from random import randint

class Contato:
    def __init__(self):
        self.__contato = []

    @property
    def contato(self):
        return self.__contato

    def adicionarContato(self, valor):
        self.__contato.append(valor)

    def listarContato(self):
        print('Contatos:')
        for i in self.contato:
            print(f'  {i}')

class Endereco:
    def __init__(self, codigo, rua, numero, bairro, cidade, estado, cep):
        self.__codigo = codigo
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado 
        self.__cep = cep

    @property
    def codigo(self):
        return self.__codigo    

    def listarEndereco(self):
        print(f'Endereco: {self.__rua}, n {self.__numero}, {self.__bairro}, {self.__cidade} - {self.__estado} - {self.__cep}')

class Pessoa:
    def __init__(self, codigo, nome, dt_nasc, endereco):
        self.__codigo = codigo
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__endereco = endereco
        self.__contato = Contato()
        

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):

        self.__codigo = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco.listarEndereco()

    @property
    def dt_nasc(self):
        return self.__dt_nasc

    def cadastrarContato(self, contato):
        self.__contato.adicionarContato(contato)

    def listarPessoa(self):
        print(f'Codigo: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.dt_nasc}')
        self.endereco
        self.__contato.listarContato()

class PessoaJuridica(Pessoa):
    def __init__(self, codigo, nome, dt_nasc, endereco, cnpj, tipo):
        super().__init__(codigo, nome, dt_nasc, endereco)
        self.__cnpj = cnpj
        self.__tipo = tipo

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def tipo(self):
        return self.__tipo

    def listarPessoaJuridica(self):
        print(f'CNPJ: {self.cnpj}')
        print(f'Enquadramento: {self.tipo}')
        super().listarPessoa()

class PessoaFisica(Pessoa):
    def __init__(self, codigo, nome, dt_nasc, endereco, cpf, sexo):
        super().__init__(codigo, nome, dt_nasc, endereco)
        self.__cpf = cpf
        self.__sexo  = sexo

    @property
    def cpf(self):
        return self.__cpf

    @property
    def sexo(self):
        return self.__sexo

    def listarPessoaFisica(self):
        print(f'CPF: {self.cpf}')
        print(f'Sexo: {self.sexo}')
        super().listarPessoa()