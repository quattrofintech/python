from tkinter import *
from tkinter import messagebox

tl = Tk()
tl.geometry('500x500+1200+100')

def limparCampo():
    txtNum1.delete(0, END)
    txtNum2.delete(0, END)
    txtNum1.focus()

def verificaValor():
    if len(txtNum1.get().strip()) < 1:
        messagebox.showwarning(title='Mensagem', message='Digite um número')
        return False
    if not txtNum1.get().strip().isnumeric():
        messagebox.showerror(title='Mensagem', message='Digite um número')
        return False
    if len(txtNum2.get().strip()) < 1:
        messagebox.showwarning(title='Mensagem', message='Digite um número')
        return False
    if not txtNum2.get().strip().isnumeric():
        messagebox.showerror(title='Mensagem', message='Digite um número')
        return False
    return True

def somar():
    # showerror, showwarning, showinfo
    if verificaValor():
        soma = int(txtNum1.get()) + int(txtNum2.get())
        lblResultado['text'] = f'{txtNum1.get()} + {txtNum2.get()} = {soma}'
        limparCampo()

        #print(txtPassword.get())

def subtrair():
    # showerror, showwarning, showinfo
    if verificaValor():
        soma = int(txtNum1.get()) - int(txtNum2.get())
        lblResultado['text'] = f'{txtNum1.get()} - {txtNum2.get()} = {soma}'
        limparCampo()

def multiplicar():
    # showerror, showwarning, showinfo
    if verificaValor():
        soma = int(txtNum1.get()) * int(txtNum2.get())
        lblResultado['text'] = f'{txtNum1.get()} x {txtNum2.get()} = {soma}'
        limparCampo()

def dividir():
    # showerror, showwarning, showinfo
    if verificaValor():
        if int(txtNum2.get()) != 0:
            soma = int(txtNum1.get()) / int(txtNum2.get())
            lblResultado['text'] = f'{txtNum1.get()} / {txtNum2.get()} = {soma}'
            limparCampo()
        else:
            messagebox.showerror(title='Mensagem', message='Não pode ser dividido por 0')
            limparCampo()
            lblResultado['text'] = ''


# _________ LAYOUT __________ #
txtNum1 = Entry(tl)
txtNum2 = Entry(tl)
#txtPassword = Entry(tl, show='*') # Campo de senha

btnSomar = Button(tl, text='Somar', command=somar)
btnSubtrair = Button(tl, text='Subtrair', command=subtrair)
btnMultiplicar = Button(tl, text='Multiplicar', command=multiplicar)
btnDividir = Button(tl, text='Dividir', command=dividir)

lblResultado = Label(tl)

# ________ EXIBIR  __________ #
txtNum1.pack()
txtNum1.focus()
txtNum2.pack()

btnSomar.pack()
btnSubtrair.pack()
btnMultiplicar.pack()
btnDividir.pack()

lblResultado.pack()
lblResultado['font'] = 'Arial 20'
#txtPassword.pack() 

tl.mainloop()