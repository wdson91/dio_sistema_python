# Dados iniciais
usuarios = []
contas_correntes = []
numero_conta = 1

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = cpf.replace(".", "").replace("-", "")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")

# Função para cadastrar uma nova conta corrente
def cadastrar_conta_corrente(usuario):
    global numero_conta
    
    agencia = "0001"
    
    nova_conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    
    contas_correntes.append(nova_conta)
    numero_conta += 1
    print("Conta corrente criada com sucesso.")

# Função para realizar um saque em uma conta corrente
def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo + limite:
        print("Saldo insuficiente.")
        return
    
    if numero_saques >= limite_saques:
        print("Limite de saques atingido.")
        return
    
    saldo -= valor
    extrato.append(f"Saque de R${valor}")
    numero_saques += 1
    
    print("Saque realizado com sucesso.")
    return saldo, extrato

# Função para realizar um depósito em uma conta corrente
def deposito(saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito de R${valor}")
    
    print("Depósito realizado com sucesso.")
    return saldo, extrato

# Função para exibir o extrato de uma conta corrente
def extrato(saldo, extrato):
    print(f"Saldo: R${saldo}")
    print("Extrato:")
    for movimento in extrato:
        print(movimento)

# Exemplo de uso
cadastrar_usuario("João da Silva", "01/01/1990", "123.456.789-00", "Rua A, 123 - Bairro X - Cidade/UF")
cadastrar_conta_corrente(usuarios[0])

saldo = 1000.0
extrato = []
limite = 500.0
numero_saques = 0
limite_saques = 3

saldo, extrato = saque(saldo, 200.0, extrato, limite, numero_saques, limite_saques)
saldo, extrato = deposito(saldo, 500.0, extrato)
extrato(saldo, extrato)
