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


# Aula

### Cliente
    nome 
    cpf
---
    comprar()
    falar()

### Funcionario
    nome
    cpf
---
    falar()
    vender()


# CASA

## PROJETO DA ESCOLA 

### Professor
    - atr:class materia = ['Matemática', 'Português', 'História', 'Química', 'Física', 'Geografia']
    - nome: str
    - cpf: str
    - materia: int
--- 
    + listar_professor()


### Aluno
    - nome: str
    - ano_nascimento: int
    - ano_escolar: int
--- 
    + listar_aluno()
    + alterar_ano_escolar()
    + idade_aluno()

