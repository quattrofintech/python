from classe import Cliente
from classe import Funcionario
from classe import Animal


#   CLIENTE 

c = Cliente('Gabriel Oliveira', 'M', '(21) 9 87654321', 'Rua F, 123, bairro, cidade, estado, 26789-090')
c.atualizar_endereco('Rua Efe, 321, Bairro, Cidade, ESTADO, CEP')
c.atualizar_telefone('219123456798')
# c.listar_cliente()

#   FUNCIONARIO


f = Funcionario('Julia', 'F', '21912345678', 'Rua tal, numero tal', 40)
f.adicionar_horas_trabalhadas(40)
f.adicionar_horas_trabalhadas(-40)
f.calcular_salario()
# f.listar_funcionario()

#   Animal

a = Animal('Tofy', 'M', 3, 0.3)
a.adicionar_peso(0.5)
a.listar_animal()