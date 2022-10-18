'''
    1) Identifique os dados de entrada, processamento e saída no algoritmo abaixo
        • Receba código da peça
        • Receba valor da peça
        • Receba Quantidade de peças
        • Calcule o valor total da peça (Quantidade * Valor da peça)
        • Mostre o código da peça e seu valor total
'''

pecas = [
    {
        'codigo': 654321,
        'descricao': 'Pneus',
        'preco': 85.69,
        'qnt': 100,
        'stqMin': 15
    },
    {
        'codigo': 789456,
        'descricao': 'Volante',
        'preco': 23.32,
        'qnt': 80,
        'stqMin': 5
    },
    {
        'codigo': 789456,
        'descricao': 'Volante',
        'preco': 23.32,
        'qnt': 80,
        'stqMin': 5
    },
]

totalEstoque = 0
for peca in pecas:
    totalEstoque += peca['qnt'] * peca['preco']
    print(f"{peca['codigo']} - {peca['descricao']} R$ {peca['qnt'] * peca['preco']}")

print(f'Total Estoque R$ {totalEstoque}')