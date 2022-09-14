from pessoa import Funcionario, Veiculo

uno = Veiculo('Fiat Uno', 'KTR65F7')

func1 = Funcionario('Thiago Silva', '12/03/2000', uno)

func1.addDepend('Pedro Henrique', '08/06/2014', 'Filho')
func1.addDepend('Lucia Batista Silva', '01/02/2000', 'Esposa')

func1.exibirFuncionario()