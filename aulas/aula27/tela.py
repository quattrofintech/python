from tkinter import *

telaInicial = Tk() # Instanciar 
telaInicial['bg'] = '#cccccc' # alterar a cor de fundo
telaInicial.title('Home') # Alterar title

largura = 850 # altura do programa
altura = 650 # largura do programa
larguraUser = telaInicial.winfo_screenwidth() # 1920 - 850 = 1070 / 2 = 535
alturaUser = telaInicial.winfo_screenheight()
print(larguraUser, alturaUser) # Tela do Usuario
larguraX = int((larguraUser - largura)/2)
alturaY = int((alturaUser - altura)/2)
telaInicial.geometry(f'{largura}x{altura}+{larguraX}+{alturaY}')
telaInicial.resizable(False, False) # 
telaInicial.minsize(850, 650)
telaInicial.maxsize(1920, 1080)
# telaInicial. ('iconic') #zoomed / iconic

labelUsu = Label(telaInicial, text='Usuário: ')
labelUsu.pack()
labelSenha = Label(telaInicial, text='Senha: ')
labelSenha.pack()

msg = 'Olá, mundo! '
def entrar():
    #print('Olá, Mundo!')
    labelUsu.config(text='greenTerror')
    labelSenha.config(text='***************')
    labelMsg.config(text='Entre com o usuário e senha corretos!')

btnEntrar = Button(telaInicial, text='Entrar', command=entrar) # Cria instancia do botão
btnEntrar.pack() # 

labelMsg = Label(telaInicial)
labelMsg.pack()




# ultima Linha
telaInicial.mainloop() # abre a tela

