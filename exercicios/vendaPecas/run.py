# IMPORTs
from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

# DEFs
def msg(msg):
    messagebox.showinfo(title='Informação', message=msg)

def iniciarComboProdutos():
    global cmbProdutos
    cmbProdutos.append('SELECIONE UM PRODUTO')
    for produto in produtos:
        cmbProdutos.append(f"{produto['codigo']}_{produto['descricao']}")
        # ['654321_Pneus', '789456_Graxa', '987561_Volante']

def inserirProduto():
    if  slctProdutos.current() == 0:
        msg('Selecione um PRODUTO')
    else:
        print('Produto Inserirdo com Sucesso')
        #slctProdutos.set('SELECIONE UM PRODUTO')
        try:
            qnt = int(txtQnt.get())
        except:
            msg('Insira uma QUANTIDADE válida')
            txtQnt.delete(0, END)
            txtQnt.insert(0, 1)
            txtQnt.focus()
        else:
            codigo = slctProdutos.get().split('_')
            codigo = int(codigo[0])
            if verificarQuantidade(codigo, qnt):
                try:
                    ps = retornarProdutoCompleto(codigo)
                except:
                    pass
                else:
                    print(ps[0])
                    print(ps[1])
                    print(ps[2])
                    #print(ps[3])
                    #print(ps[4])
                    print(f"COD {ps[0]} - {ps[1]} - QNT {qnt} x R${ps[2]} ..... R${qnt*ps[2]}")
            else:
                msg('Estoque INSUFICIENTE')

def verificarQuantidade(codigo, qnt):
    for produto in produtos:
        if produto['codigo'] == codigo:
            if produto['qnt'] >= qnt:
                return True
    return False

def retornarProdutoCompleto(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return [
                produto['codigo'],
                produto['descricao'],
                produto['preco'],
                produto['qnt'], 
                produto['stqMin']
            ]
    
# VARs
produtos = [
    {
        'codigo': 654321,
        'descricao': 'Pneus', # 654321_Pneus
        'preco': 85.69,
        'qnt': 100,
        'stqMin': 15
    },
    {
        'codigo': 789456,
        'descricao': 'Graxa',
        'preco': 23.32,
        'qnt': 80,
        'stqMin': 5
    },
    {
        'codigo': 987561,
        'descricao': 'Volante',
        'preco': 23.32,
        'qnt': 20,
        'stqMin': 5
    },
]
cmbProdutos = []

# GUI
tela = Tk()
janelaX = 900
janelaY = 600
telaX = tela.winfo_screenwidth()
telaY = tela.winfo_screenheight()
posX = int((telaX - janelaX) / 2)
posY = int((telaY - janelaY) / 2) - 10
tela.geometry(f'{janelaX}x{janelaY}+{posX}+{posY}')
tela.resizable(False, False) # (X , Y)

slctProdutos = Combobox(tela, font='Arial 18')
iniciarComboProdutos()
slctProdutos['values'] = cmbProdutos
slctProdutos.set('SELECIONE UM PRODUTO')

txtQnt = Entry(tela, font='Arial 18')

btnInserir = Button(tela, text='INSERIR', font='Arial 14', command=inserirProduto)

# EXIBIR
slctProdutos.grid(row=0, columnspan=3, padx=10, pady=10)
slctProdutos.focus()

Label(tela, text='QNT', font='Arial 14').grid(row=1, column=0, padx=10, pady=10)
txtQnt.grid(row=1, column=1, padx=10, pady=10)
txtQnt.insert(0, 1)

btnInserir.grid(row=2, column=0, padx=10, pady=10)

tela.mainloop()


