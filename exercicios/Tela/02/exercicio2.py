''' 
    2 -  Criar um tela de cadastro
        2.1 - Nome, Email, Telefone, Endereço, senha
        2.2 - Botão de cadastro
        2.3 - Verificar se existem campos vazios 
        2.3.1 - Mensagem de erro se houver campos vazios
        2.3.2 - Se tudo correto informar em um box que o usuario foi criado
'''

from tkinter import *
from tkinter import messagebox

def cadastrar():
    if txtNome.get().strip() == '':
        messagebox.showerror(message='Preencha o campo NOME corretamente')
    elif txtEmail.get().strip() == '':
        messagebox.showerror(message='Preencha o campo EMAIL corretamente')
    elif txtTelefone.get().strip() == '':
        messagebox.showerror(message='Preencha o campo TELEFONE corretamente')
    elif txtEndereco.get().strip() == '':
        messagebox.showerror(message='Preencha o campo ENDEREÇO corretamente')
    elif txtSenha.get().strip() == '':
        messagebox.showerror(message='Preencha o campo SENHA corretamente')
    elif len(txtSenha.get().strip()) < 6:
        messagebox.showwarning(message='Senha deve conter no minimo 6 caracteres')
    else:
        limparCampos()
        #messagebox.showinfo(message='Usuário cadastrado com sucesso!')
        res = messagebox.askyesno(message='Deseja Finalizar o Programa?')
        if res:
            tela.destroy()

def limparCampos():
    txtNome.delete(0, END)
    txtEmail.delete(0, END)
    txtTelefone.delete(0, END)
    txtEndereco.delete(0, END)
    txtSenha.delete(0, END)

tela = Tk()
tela.title('Cadastro de usuário')
tela.resizable(False, False)

Label(tela, text='CADASTRO', font='Arial 30', padx=10, pady=10).grid(row=0, columnspan=2)
Label(tela, text='Nome', anchor=W, justify=LEFT).grid(row=1, column=0)
Label(tela, text='Email', anchor=W, justify=LEFT).grid(row=2, column=0)
Label(tela, text='Telefone', anchor=W, justify=LEFT).grid(row=3, column=0)
Label(tela, text='Endereço', anchor=W, justify=LEFT).grid(row=4, column=0)
Label(tela, text='Senha', anchor=W, justify=LEFT).grid(row=5, column=0)

txtNome = Entry(tela)
txtEmail = Entry(tela)
txtTelefone = Entry(tela)
txtEndereco = Entry(tela)
txtSenha = Entry(tela, show='*')

txtNome.grid(row=1, column=1)
txtEmail.grid(row=2, column=1)
txtTelefone.grid(row=3, column=1)
txtEndereco.grid(row=4, column=1)
txtSenha.grid(row=5, column=1)
Button(tela, text='Cadastrar', command=cadastrar).grid(columnspan=2)
tela.mainloop()