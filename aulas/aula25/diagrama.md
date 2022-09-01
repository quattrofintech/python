# Classes: Relação de Composição

### Cliente
    - nome: str
    - cpf: str
    ________________________________
    + listar_cliente()

---

### Conta
    - numero: int
    - saldo: float
    - titular: Cliente
    - historico: Historico
    ________________________________
    + listar_conta()
    + sacar()
    + depositar()
    + transferir()
    + transacoes()

---

### Historico
    - transacoes: []
    ________________________________
    + adicionar_transacao()
    + listar_historico()