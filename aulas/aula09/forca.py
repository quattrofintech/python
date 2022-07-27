# JOGO DA FORCA 
from random import randint

# Criei uma lista de palavras pro jogo 
# LISTA OU VETOR 
palavras = ['Casa', 'Carro', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao', 'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa', 'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']

indice = '' # Recebe um numero aleatorio entre 0 e a quantidade total de palavras da lista
palavra_secreta =  '' # Palavra do jogo 
tentativa = [] # LISTA DA PALAVRA  _ _ _ _ _  -> P _ _ T _
chutes = [] # LISTA DE CHUTES ERRADOS -> W, S, M, J, P


def exibirMsg(msg):
    print(msg)

def encontraLetra(chute): # O
    temLetra = False
    for i, letra in enumerate(palavra_secreta): # M O T O
        if(chute.upper() == letra.upper()):
            tentativa[i] = chute.upper()
            temLetra = True
    return temLetra

def jogar():
    tentativas = 5
    while(True):
        chute = input('Digite uma letra R: ') # O
        if(encontraLetra(chute)):
            exibirMsg(tentativa)
        else:
            exibirMsg(f'Letra {chute} não encontrada')
            chutes.append(chute.upper())
            exibirMsg(chutes)
            tentativas -= 1
            exibirMsg(f'Restam {tentativas} tentativas')
            exibirMsg(tentativa)
        
        if(verificaVitoria()):
            exibirMsg('PARABÉNS!!! VOCÊ VENCE')
            break

        if(tentativas <= 0):
            exibirMsg('VOCÊ PERDEU ;( \nJOGUE NOVAMENTE!')
            exibirMsg(f'A palavra secreta era {palavra_secreta.upper()}')
            break

def verificaVitoria():
    if( '_' in tentativa):
        return False
    else:
        return True

def iniciaJogo():
    global indice
    indice = randint(0, len(palavras) - 1) # Recebe um numero aleatorio entre 0 e a quantidade total de palavras da lista
    global palavra_secreta
    palavra_secreta =  palavras[indice] # Palavra do jogo 
    global tentativa
    tentativa = [] # LISTA DA PALAVRA  _ _ _ _ _  -> P _ _ T _
    global chutes
    chutes = [] # LISTA DE CHUTES ERRADOS -> W, S, M, J, P

    for i in range(len(palavra_secreta)):
        tentativa.append('_')

def escolha():
    while(True): # continuar == True
        iniciaJogo()
        exibirMsg('**** JOGO DA FORCA ****')
        menu = int(input(' 1 - Jogar \n 2 - Sair \n R:'))
        if(menu == 1):
            jogar()
        else:
            exibirMsg('Tchau!!!!')
            break





escolha()