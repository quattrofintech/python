# IMPORTs
from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview

# DEFs
def msg(msg):
    messagebox.showinfo(title='Informação', message=msg)

def iniciarComboProdutos():
    global cmbProdutos
    cmbProdutos.append('SELECIONE UM PRODUTO')
    for produto in produtos:
        cmbProdutos.append(f"{produto['codigo']}_{produto['descricao']}")
        # ['654321_Pneus', '789456_Graxa', '987561_Volante']

def inserirProduto(event):
    print(event)
    if  slctProdutos.current() == 0:
        msg('Selecione um PRODUTO')
    else:
        #print('Produto Inserirdo com Sucesso')
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
                    tabelaCompra.insert('', END, values=(ps['codigo'], ps['descricao'], ps['preco'], qnt, qnt*ps['preco']))
                    slctProdutos.set('SELECIONE UM PRODUTO')
                    slctProdutos.focus()
                    lblTotal.config(text=f'R$ {verificarSaldo()}')
                    txtQnt.delete(0, END)
                    txtQnt.insert(0, 1)
                    #print(f"COD {ps['codigo']} - {ps['descricao']} - QNT {qnt} x R${ps['preco']} ..... R${qnt*ps['preco']}")
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
            return produto
    
def verificarSaldo():
    total = 0
    for i in tabelaCompra.get_children():
        total += float(tabelaCompra.item(i, 'values')[4])
    return round(total, 2)

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
        'descricao': 'Graxa Outros Produto Com nome Grande',
        'preco': 23.32,
        'qnt': 80,
        'stqMin': 5
    },
    {
        'codigo': 987561,
        'descricao': 'Volante',
        'preco': 58.10,
        'qnt': 20,
        'stqMin': 5
    },
]
cmbProdutos = []
headTabela = ['CODIGO', 'DESCRIÇÃO', 'R$ UNT', 'QNT', 'TOTAL']

# GUI
tela = Tk()
janelaX = 900
janelaY = 600
telaX = tela.winfo_screenwidth()
telaY = tela.winfo_screenheight()
posX = int((telaX - janelaX) / 2)
posY = int((telaY - janelaY) / 2) - 10
tela.title('AutoPeças Já')
tela.geometry(f'{janelaX}x{janelaY}+{posX}+{posY}')
tela.resizable(False, False) # (X , Y)

slctProdutos = Combobox(tela, font='Arial 18')
iniciarComboProdutos()
slctProdutos['values'] = cmbProdutos
slctProdutos.set('SELECIONE UM PRODUTO')

txtQnt = Entry(tela, font='Arial 18')

btnInserir = Button(tela, text='INSERIR', font='Arial 14')

tabelaCompra = Treeview(tela, columns=(0, 1, 2, 3, 4), show='headings')

for i in range(len(headTabela)):
    tabelaCompra.heading(i, text=headTabela[i])
    tabelaCompra.column(i, width=len(headTabela[i])*15, minwidth=50)

lblTotal = Label(tela, font='Arial 16')

# EXIBIR
#tela.bind('<F7>', inserirProduto)

slctProdutos.grid(row=0, columnspan=3, padx=10, pady=10)
slctProdutos.focus()

Label(tela, text='QNT', font='Arial 14').grid(row=1, column=0, padx=10, pady=10)
txtQnt.grid(row=1, column=1, padx=10, pady=10)
txtQnt.bind('<Return>', inserirProduto) # Enter / Leave / FocusIn / FocusOut
txtQnt.insert(0, 1)

btnInserir.grid(row=2, column=0, padx=10, pady=10)
btnInserir.bind("<Button-1>", inserirProduto) # 
btnInserir.bind("<Button-3>", inserirProduto) # 
btnInserir.bind("<Return>", inserirProduto) # 

tabelaCompra.grid(row=3, columnspan=3, padx=10, pady=10)

lblTotal.grid(row=4, columnspan=3, padx=10, pady=10)


tela.mainloop()


