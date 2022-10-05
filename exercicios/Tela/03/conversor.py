from tkinter import *
from tkinter.ttk import Combobox


tela = Tk()
tela.title('Conversor de temperaturas')
Label(tela, text='Conversor', font='Arial 18').grid(row=0, columnspan=4)
Label(tela, text='Temperatura').grid(row=1, column=0, sticky=W)

temperatura = Entry(tela)
temperatura.grid(row=2, columnspan=3, sticky=W+E)

def verificar():
    if len(temperatura.get().strip()) > 0:
        return True
    return False

def limparCampo():
    temperatura.delete(0, END)
    temperatura.focus()

def celFah():
    # C x 1.8 + 32
    if verificar():
        calc = float(temperatura.get().strip()) * 1.8 + 32
        lblExibir.config(text=f'{round(calc,2)} ºF')
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Celsius > Fahrenheit', command=celFah).grid(row=3, column=0)

def fahCel():
    # (F - 32) / 1.8
    if verificar():
        calc = (float(temperatura.get().strip()) - 32)  / 1.8
        lblExibir.config(text=f'{round(calc,2)} ºC')
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Fahrenheit > Celsius', command=fahCel).grid(row=3, column=1)

def celKel():
    # C + 273.15
    if verificar():
        calc = float(temperatura.get().strip()) + 273.15
        lblExibir.config(text=f'{round(calc,2)} K')
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Celsius > Kelvin', command=celKel).grid(row=3, column=2)

def kelCel():
    # K - 273.15
    if verificar():
        calc = float(temperatura.get().strip()) - 273.15
        lblExibir.config(text=f'{round(calc,2)} ºC')
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Kelvin > Celsius', command=kelCel).grid(row=4, column=0)

def kelFah():
    if verificar():
        calc = float(temperatura.get().strip()) - 273.15
        calc = calc * 1.8 + 32 
        lblExibir.config(text=f'{round(calc,2)} ºF')
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Kelvin > Fahrenheit', command=kelFah).grid(row=4, column=1)

def fahKel():
    if verificar():
        calc = (float(temperatura.get().strip()) - 32)  / 1.8
        calc = calc + 273.15
        lblExibir.config(text=f'{round(calc,2)} K')
        limparCampo()
    else:
        limparCampo()
Button(tela, text='Fahrenheit > Kelvin', command=fahKel).grid(row=4, column=2)

lista = ['Celsius > Fahrenheit', 'Celsius > Fahrenheit', 'Celsius > Fahrenheit', 'Celsius > Fahrenheit', 'Celsius > Fahrenheit','Celsius > Fahrenheit']
box = Combobox(tela, values=lista)
box.grid()
lblExibir = Label(tela, font='Arial 32')
lblExibir.grid(columnspan=3)

tela.mainloop()