from empresa import Chefe, Comissionado

c = Chefe()
c.adicionarEmpregado('Iago Batista Jr', 
'Rua abc, Centro, Belo Horizonte - MG')
c.adicionarSalario('500')
c.adicionarSalario('100.489')
c.exibirEmpregado()
c.calcularSalario()



com = Comissionado(2000, 68, 12)
com.adicionarEmpregado('Pedro Junior.', 'Rua Cba, 46, ASUhduashdum, SAd - SP')
com.exibirEmpregado()
print(f'Salário: R$ {com.calcularSalario()}')


''' 
    Classes
        - Explicações
        - Exemplos
        - pesquisas 
    
    Instacia / Objetos
        - Explicações
        - Exemplos
        - pesquisas 
    
    Encapsulamento
        - Explicações
        - Exemplos
        - pesquisas 
    
    POO
        - Explicações
        - Exemplos
        - pesquisas 

'''