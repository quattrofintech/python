''' 
    CRIAR UMA LOCADORA 

    O Programa deve criar duas classes FILME e AUTOR
    
    Classe FILME 
        (nome, autor, ano, tema, alugado(boolean))
        - Classe Filme deve conter a referencia de um autor
        - Filme deve os metodos
            - Alugar Filme 
            - Devolver filme
        O filme não pode ser alugado se ele ja estiver alugado e nem devolvido se ja estiver na loja
        EXIBIÇÃO
                FILME: O PODEROSO CHEFÃO 
                AUTOR: COD AUTOR - NOME AUTOR 
                ANO: 1992
                TEMA: TEMA
                ALUGADO:  True / False
    Classe Autor
        (codigo, nome)

'''

from autor import Autor
from filme import Filme

autor1 = Autor(1, 'Nome Completo')

filme1 = Filme("Thor", autor1, "2022", "Herois / Aventura")

filme1.alugarFilme()
filme1.devolverFilme()
filme1.listarFilme()

autor2 = Autor(2, 'Cristopher Nolan')

filme2 = Filme("Batman: Cavaleiro das trevas", autor2, "2013", "Herois / Aventura")

filme2.alugarFilme()
filme2.listarFilme()