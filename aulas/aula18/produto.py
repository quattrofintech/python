from random import randint

class Produto:
    lista_tipos = ["Alimentação", "Limpeza", "Pets"]
    
    def __init__(self, n, p, qnt, t): # this
        self.codigo = self.gerarCodigoProduto()
        self.nome = n
        self.preco = p
        self.qntEstoque = qnt
        self.tipo = t

    def listarProduto(self):
        print(f'Codigo: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'R$: {self.preco}')
        print(f'Qnt Estoque: {self.qntEstoque}')
        print(f'Tipo: {self.retornarTipo(self.tipo)}')
        print('--' * 15)

    def valorEstoque(self):
        return print(f"Total Estoque R$ {self.preco * self.qntEstoque}")

    def venderProduto(self, qnt):
        if qnt > self.qntEstoque:
            return print('Quantidade em estoque insuficiente!!!')
        self.qntEstoque -= qnt
        self.listarProduto()
        print(f'Venda realizada com sucesso! Restam {self.qntEstoque} produtos em estoque')
        self.verificarComprarMais(self.qntEstoque)

    @classmethod
    def listarTipos(cls):
        print(cls.lista_tipos)

    @classmethod
    def retornarTipo(cls, tipo):
        return cls.lista_tipos[tipo - 1]

    @staticmethod
    def verificarComprarMais(qnt):
        if qnt < 5:
            print('Compre mais produtos!')
        else:
            print('Ainda há produtos no estoque!') 

    @staticmethod    
    def gerarCodigoProduto():
        return randint(10000, 99999)




