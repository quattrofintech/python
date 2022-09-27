from tkinter import *

def limparCampo():
    txtCapital.delete(0, END)
    txtTaxa.delete(0, END)
    txtTempo.delete(0, END)
    txtCapital.focus()

def calcular():
    # J = C ∙ i ∙ t
    # M = C + J
    c = float(txtCapital.get())
    i = float(txtTaxa.get()) / 100
    t = int(txtTempo.get())
    j = c * i * t
    m = c + j
    exibir = f'Capital: R$ {c} \ntaxa: {i}% \nTempo: {t} meses \nJuros: R$ {j} \nMontante: R$ {m}'
    lblExibir.config(text=exibir)
    limparCampo()


largura = 500
altura = 500

tl = Tk()
tl.resizable(False, False)
tl.title('Calculadora Juros Simples')

larguraUser = tl.winfo_screenwidth()
alturaUser = tl.winfo_screenheight()
posx = int((larguraUser - largura) / 2)
posy = int((alturaUser - largura) / 2 - 20)
tl.geometry(f'{largura}x{altura}+{posx}+{posy}')

txtCapital = Entry(tl)
txtTaxa = Entry(tl)
txtTempo = Entry(tl)

btnCalcular = Button(tl, text='Calcular', command=calcular)

lblTitulo = Label(tl, text='Calculadora Juros Simples', font='Arial 20')
lblExibir = Label(tl, font='Arial 18')

lblTitulo.grid(row=0, columnspan=3)

Label(tl, text='Capital', font='Calibri 12').grid(row=1, column=0)
Label(tl, text='Taxa', font='Calibri 12').grid(row=1, column=1)
Label(tl, text='Tempo', font='Calibri 12').grid(row=1, column=2)

txtCapital.grid(row=2, column=0)
txtTaxa.grid(row=2, column=1)
txtTempo.grid(row=2, column=2)

btnCalcular.grid(row=3, columnspan=3, sticky=W+E)

lblExibir.grid(row=4, columnspan=3)

tl.mainloop()