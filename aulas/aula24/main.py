from classe import Produto, CarrinhoCompra

agua = Produto('Água 500ml', 2.50 )
cerveja = Produto('Skola 350ml', 4.00)
refrigerante = Produto('Convença! 2l', 3.50)
biscoito = Produto('Biscoito', 6.25)
#agua.listarProduto()

cc = CarrinhoCompra()
cc.adicionar_produto(agua)
cc.adicionar_produto(cerveja)
cc.adicionar_produto(biscoito)
cc.adicionar_produto(refrigerante)
cc.listar_produtos()
cc.adicionar_produto(agua)
cc.adicionar_produto(cerveja)
cc.adicionar_produto(refrigerante)
cc.adicionar_produto(biscoito)
cc.finalizar_compra()