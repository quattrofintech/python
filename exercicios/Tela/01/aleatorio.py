from random import randint
from tkinter import *


# FUNÇÕES
def girar():
    valor = randint(1, 6)
    lblDado.config(text=valor)

# VARIAVEIS
largura = 300
altura = 300


# PROGRAMA
tk = Tk()
tk.title('Dado')
tk.resizable(False, False)

larguraUser = tk.winfo_screenwidth()
alturaUser = tk.winfo_screenheight()
posx = int((larguraUser - largura) / 2)
posy = int((alturaUser - largura) / 2 - 20)
tk.geometry(f'{largura}x{altura}+{posx}+{posy}')

Button(tk, text='Girar', font='Calibri 25', command=girar).pack()

lblDado = Label(tk, font='Arial 200')
lblDado.pack()
# RODAR TELA
tk.mainloop()