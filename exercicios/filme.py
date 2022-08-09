class Filme:
    def __init__(self, nome, autor, ano, tema, alugado=False):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.tema = tema
        self.alugado = alugado
        print('Filme foi cadastrado com sucesso!')

    #(nome, autor, ano, tema, alugado(boolean))

    def alugarFilme(self):
        if self.alugado:
            return print(f'{self.nome} já está alugado')
        self.alugado = True
        return print(f'{self.nome} foi alugado com sucesso!')

    def devolverFilme(self):
        if not self.alugado:
            return print(f'{self.nome} já foi devolvido')
        self.alugado = False
        return print(f'{self.nome} foi devolvido com sucesso!')
    
    def listarFilme(self):
        print('FILME')
        print('-' * 30)
        print(f'Filme: {self.nome}')
        print(f'Autor: COD:{self.autor.codigo}  - Nome: {self.autor.nome}')
        print(f'Ano: {self.ano}')
        print(f'Alugado: {self.alugado} \n')

        

