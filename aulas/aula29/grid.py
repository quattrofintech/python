from tkinter import *

tela = Tk()
tela.title('Primeira aula de Grid')
tela.geometry('+1200+100')

lbl1 = Label(tela, width=30, justify='right', text='Nome', )
lbl2 = Label(tela, width=30, justify='right', text='E-mail', )
lbl3 = Label(tela, width=30, justify='right', text='Senha', )

btnCadastrar = Button(tela, text='Cadastrar')

txtNome = Entry(tela)
txtEmail = Entry(tela)
txtSenha = Entry(tela, show='*')

lbl1.grid(row=0, column=0, sticky=W)
lbl2.grid(row=1, column=0, sticky=W)
lbl3.grid(row=2, column=0, sticky=W)

txtNome.grid(row=0, column=1)
txtEmail.grid(row=1, column=1)
txtSenha.grid(row=2, column=1)

btnCadastrar.grid(columnspan=2, sticky='we')

tela.mainloop()

''' 
        0 ->    0  |  1  |  2
        1 ->    0  |  1  |  2
        2 ->    0  |  1  |  2
        3 ->    0  |  1  |  2
        3 ->     button  |  2
'''


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


    2 -  Criar um tela de cadastro
        2.1 - Nome, Email, Telefone, Endereço, senha
        2.2 - Botão de cadastro
        2.3 - Verificar se existem campos vazios 
        2.3.1 - Mensagem de erro se houver campos vazios
        2.3.2 - Se tudo correto informar em um box que o usuario foi criado

'''