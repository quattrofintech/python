# .txt

'''
    r -> Ler
    W -> Escrever
    a -> Acrescentar
    r+ -> Ler e Acrescentar
'''
caminho = './aulas/aula31'

# Escrever
'''with open(f'{caminho}/teste.txt', 'w') as arq:
    arq.write('Posso escrever o que eu quiser!')'''

# Acrescentar
'''with open(f'{caminho}/teste.txt', 'a') as arq:
    arq.write('Linhas - Amasdijas')'''

# Ler
'''with open(f'{caminho}/teste.txt', 'r') as arq:
    texto = []
    for linha in arq:
        texto.append(linha)
    texto[0] = 'Linha 1\n'''

''' 
    texto -> Lista [linha1, linha2, ...]

'''
#for i in texto:
    #print(i)

'''with open(f'{caminho}/teste.txt', 'w') as arq:
    for i in texto:
        arq.write(i)'''

# Ler e Acrescentar     
with open(f'{caminho}/teste.txt', 'r+') as arq:
    for i in arq:
        print(i)
    arq.write('Linha 4\n')