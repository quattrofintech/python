''' 
12. Um posto está vendendo combustíveis com a seguinte tabela de descontos:  

Álcool: R$ 4.89
- Até 20 litros: desconto de 3% por litro
- Acima de 20 litros: Desconto de 5% por litro.

Gasolina: R$ 6.58
- Até 20 litros: desconto de 4% por litro
- Acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool. G-gasolina), calcule e imprima o valor a ser pago pelo cliente.  
'''


alcool = 4.89
gasolina = 6.58

tipo_combustivel = input('Digite o tipo de combustível: (A - Álcool, G - Gasolina) ')[0].lower()
litros = int(input('Digite a quantidade comprada em litros: '))

total = 0
preco = 0

if tipo_combustivel == 'a':
    print('Álcool')
    if litros <= 20:
        preco = alcool * 0.97 # 3% = 0.03 -> 0.97
    else:
        preco = alcool * 0.95 # 5% = 0.05 -> 0.95
elif tipo_combustivel == 'g':
    print('Gasolina')
    if litros <= 20:
        preco = gasolina * 0.96 # 4% = 0.04 -> 0.96
    else:
        preco = gasolina * 0.94 # 6% = 0.06 -> 0.94
else:
    print('Combustível desconhecido')

total = preco * litros
print(f'Total R$ {total}')