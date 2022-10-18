'''while True:
    print('Tratando Erros')
    menu = input('1 - Opção1 \n2 - Opção2 \n3 - Opção3 \n R: ')
    if menu > 3:
        break'''

#print(x)

#divsao = 15 / 0
#print(divsao)

lista = [0, 1, 2, 3, 4, 5]
#x = 10
'''try:
    #print(x)
    #print(lista[6])
    #divisao = 15 / 0
    #menu = int(input('1 - Opção1 \n2 - Opção2 \n3 - Opção3 \n R: '))
    #with open('texto.md', 'r') as arquivo:
        #print(arquivo)
except NameError:
    print('Variavel não encontrada')
except IndexError:
    print('Indice da lista não encontrado')
except ZeroDivisionError:
    print('O divisor não pode ser zero')
except ValueError:
    print('Digite apenas números inteiros')
except FileNotFoundError:
    print('Arquivo não encontrado')
except Exception as error:
    print('Exception Default', error.__class__)
    print('Exception Default', error)
except:
    print('Erro')
else: # Se não houver error entra no else
    print('Arquivo Lido')
'''


import urllib.request
try:
    site = urllib.request.urlopen('https://github.com/')
except urllib.error.URLError:
    print('Site não encontrado')
except Exception as error:
    print(error)
else:
    tags = str(site.read()).split('>') # Lista de tags
    try:
        with open('cats.html', 'w') as arquivo:
            for i in tags :
                valor = i.replace("b'", '').replace("'>", "").replace("\n", "").replace('\n', '')
                arquivo.write(f'{valor}>\n')
    except TypeError:
        print('Erro de tipo')