''' 
1 - Criar um tela de login que inicialize no centro de todas as telas
        1.1 - Tem que ter Username
        1.2 - Senha (***)
        1.3 - Botão logar
        1.3.1 - Ao logar verificar usuarios e senhas que ja estaram definidos como certos
        1.3.2 - Se usuario incorreto, informar com um box, apagar o campo e colocar foco no user
        1.3.3 - Se senha incorreta, informar com um box, apagar o campo e colocar foco no user
        1.3.4 - Se usuario e senha corretos, informar com um label que o usuario esta logado

        user = 'AkioHash'
        senha = 'Hash123'
'''
# IMPORTS 
from tkinter import *
from tkinter import messagebox

# Funções
def logar():
    userName = txtUsername.get().strip()
    userPassword = txtPassword.get().strip()
    if userName == '':
        messagebox.showwarning(title='Mensagem', message='Digite o seu login')
    elif userPassword == '':
        messagebox.showwarning(title='Mensagem', message='Digite a sua senha')
    elif userName != 'Akio':
        messagebox.showerror(title='Mensagem', message='Login Incorreto')
        limparUsername()
    elif userPassword != '$AH3214':
        messagebox.showerror(title='Mensagem', message='Senha Incorreta')
        limparPassword()
    else:
        print(userName, userPassword)
        lblCon.config(text='CONECTADO!')
        limparUsername()
        limparPassword()
        lblCon.focus()


def limparUsername():
    txtUsername.delete(0, END)
    txtUsername.focus()

def limparPassword():
    txtPassword.delete(0, END)
    txtPassword.focus()
# Variaveis
largura = 500
altura = 200

loginCorreto = 'Akio'
senhaCorreta = '$AH3214'

# Interface
login = Tk()
login.title('Plataforma')
larguraUser = login.winfo_screenwidth()
alturaUser = login.winfo_screenheight()
posx = int((larguraUser - largura)/2)
posy = int((alturaUser - altura)/2 )
print(posx, posy)
login.geometry(f'{largura}x{altura}+{posx}+{posy}')
login.resizable(False, False)

Label(login, text='Plataforma da Empresa', font='Arial 18').pack()
lblCon = Label(login, font='Arial 20')

txtUsername = Entry(login)
txtPassword = Entry(login, show='*')

txtUsername.pack()
txtPassword.pack()

Button(login, text='Logar', command=logar).pack()
lblCon.pack()
login.mainloop()