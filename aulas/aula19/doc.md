# Funcionario
    - valor_hora_cargo = [189.56, 86.05, 35.48] : atr class
    - nome_cargo = ['Diretor', 'Gerente', 'Vendedor'] : atr class
    + nome: string
    + cargo: int
    + horas_trabalhadas : int
    - salario: float
---
    + exibir_funcionario()
    + adicionar_horas_trabalhadas()
    + calcular_salario()

--- 

# Encapsulamento
    + public 
    # protected
    - private

--- 

# CASA
## Cliente
    - codigo
    + nome
    + sexo
    + telefone
    + endereco
--- 
    + gerar_codigo_usuario()
    + atualizar_endereco()
    + atualizar_telefone()
    + listar_cliente()
    

## Funcionario
    - codigo
    + nome
    + sexo
    + telefone
    + endereco
    + horas_trabalhadas
    - salario
--- 
    + gerar_codigo_funcionario()
    + atualizar_endereco()
    + atualizar_telefone()
    + listar_funcionario()
    + adicionar_horas_trabalhadas(horas)
    + calcular_salario()


## Animais
    - animal = ['Cachorro', 'Gato', 'Tartaruga', 'Pássaro', 'Peixe']: attr classe
    - codigo
    + nome
    + sexo
    + animal: int
    + peso
--- 
    + gerar_codigo_animal()
    + listar_animal()
    + adicionar_peso(peso)