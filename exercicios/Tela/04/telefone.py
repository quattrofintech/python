from glob import glob
from tkinter import *

''' 
    Uma lista com telefones
'''
def verificarEntry():
    if len(txtTelefone.get().strip()) > 0:
        return True
    False

def addTel():
    if verificarEntry():
        ltsTelefones.insert(END, txtTelefone.get().strip().replace('-', ''))
        telefones.append(txtTelefone.get().strip().replace('-', ''))
    print(telefones)
    funcaoSalvar()

def funcaoSalvar():
    with open(f'{caminho}/chamadasPerdidas.txt', 'w', encoding='utf-8') as arquivo:
        for i in telefones:
            arquivo.write(i + ';')

def carregarChamadas():
    global telefones
    with open(f'{caminho}/chamadasPerdidas.txt', 'r') as arq:
        for linha in arq:
            telefones = linha.split(';')
        if len(telefones) > 0:
            telefones.pop()
        for i in telefones:
            ltsTelefones.insert(END, i)
    print(telefones)

caminho = './exercicios/tela/04'
telefones = []

run = Tk()
run.geometry('300x500+1490+100')
run.title('Chamdas Perdidas')
run.resizable(False, False)

txtTelefone = Entry(run, font='Arial 25')
txtTelefone.place(x=10, y=10, width=280, height=50)
Button(run, text='Adicionar', command=addTel).place(x=10, y=70, width=280, height=50)
ltsTelefones = Listbox(run, font='Arial 20')
ltsTelefones.place(x=10, y =140, width=280, height=250)
carregarChamadas()
run.mainloop()