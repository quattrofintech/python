from asyncio.windows_events import NULL
from cProfile import label
from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.geometry('500x500')
tela.resizable(False, False)
tela.title('Lista de Compras')

Label(tela, text='Lista', font='Arial 20').pack()
Label(tela, text='Item', anchor=W, justify=LEFT ).pack()

txtItem = Entry(tela)
txtItem.pack()

def limparCampo():
    txtItem.delete(0, END)
    txtItem.focus()

def adicionarItem():
    if len(txtItem.get().strip()) > 0:
        listaDeCompras.insert(END, txtItem.get().strip().upper())
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Adicionar', command=adicionarItem).pack()

Label(tela).pack()

listaDeCompras = Listbox(tela)
listaDeCompras.pack()

def deletarItem():
    index = retornaIndex()
    if index == None:
        messagebox.showerror(title='Info', message='Selecione um item')
    else:
        if messagebox.askyesno(title='Confirmação', message=f'Deseja deletar {listaDeCompras.get(ACTIVE)} ?'):
            listaDeCompras.delete(index)
            messagebox.showinfo(title='Confirmação', message='Item deletado com sucesso')
    limparCampo()
    
def retornaIndex():
    for index in listaDeCompras.curselection():
        return index
Button(tela, text='Deletar', command=deletarItem).pack()


tela.mainloop()