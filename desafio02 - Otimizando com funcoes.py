import textwrap
from datetime import date

def menu():
    menu = """\n
    ++++++++++++++++ MENU +++++++++++++++++++

    Escolha a operação bancária a ser feita:

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair 
    
    +++++++++++++++++++++++++++++++++++++++++
    
    ===>"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, data_operacao, data_extrato, data_ultima_operacao, numero_operacoes, /):

    if valor > 0 and data_ultima_operacao != data_operacao:
            data_ultima_operacao = data_operacao
            numero_operacoes = 0
            saldo += valor
            extrato += f"{data_extrato} Depósito: R$ {valor:.2f}\n"
            numero_operacoes += 1  
            print(f"+++  Depósito no valor de R$ {valor:.2f} realizado.  +++")  
        
    elif valor > 0 and numero_operacoes <= 10:
        saldo += valor
        extrato += f"{data_extrato}\tDepósito: R$ {valor:.2f}\n"
        numero_operacoes += 1
        print(f"+++  Depósito no valor de R$ {valor:.2f} realizado.  +++") 

    elif numero_operacoes > 10:
        print("!!! Você atingiu o limite máximo de operações diário (10). Tente de novo amanhã. !!!")

    else:
        print("!!! Operação falhou! O valor informado é inválido. !!!")

    return saldo, extrato, numero_operacoes, data_ultima_operacao


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, numero_operacoes, data_operacao, data_ultimo_saque, data_extrato, data_ultima_operacao):
    
    if data_ultima_operacao != data_operacao:
            numero_operacoes = 0

    if data_ultimo_saque != data_operacao:
            numero_saques = 0
    
    if valor > saldo:
        print("!!! Operação falhou! Você não tem saldo suficiente. !!!")

    elif valor > limite:
        print("!!! Operação falhou! O valor do saque excede o limite. !!!")

    elif numero_saques >= limite_saques:
        print("!!! Operação falhou! Número máximo de saques excedido. !!!")

    elif numero_operacoes > 10 and data_ultima_operacao == data_operacao:
        print("!!! Você atingiu o limite máximo de operações diário (10). Tente de novo amanhã. !!!")

    elif valor > 0 and data_operacao == data_ultimo_saque:
        saldo -= valor
        extrato += f"{data_extrato}\tSaque: R$ {valor:.2f}\n"
        numero_saques += 1
            
        if data_ultima_operacao != data_operacao:
            data_ultima_operacao = data_operacao

        numero_operacoes += 1
        print(f"+++  Saque no valor de R$ {valor:.2f} realizado.  +++")
        
    elif valor > 0 and data_operacao != data_ultimo_saque:
        saldo -= valor
        extrato += f"{data_extrato}\tSaque: R$ {valor:.2f}\n"
        numero_saques = 1

        if data_ultima_operacao != data_operacao:
            data_ultima_operacao = data_operacao
            
        numero_operacoes += 1
        data_ultimo_saque = data_operacao
        print(f"+++  Saque no valor de R$ {valor:.2f} realizado.  +++")

    else:
        print("!!! Operação falhou! O valor informado é inválido. !!!")

    return saldo, extrato, numero_operacoes, data_ultima_operacao, data_ultimo_saque, numero_saques


def exibir_extrato(saldo, data_ultima_operacao, data_operacao, /, *, extrato, numero_operacoes):

    if data_ultima_operacao != data_operacao:
        data_ultima_operacao = data_operacao
        numero_operacoes = 0
        print("\n================ EXTRATO ================")
        print("\n Não foram realizadas movimentações ainda.\n" if not extrato else extrato)
        print(f"\nSaldo em {data_operacao}:\tR$ {saldo:.2f}")
        print("==========================================")
        numero_operacoes += 1
        
    elif numero_operacoes > 10:
        print("!!! Você atingiu o limite máximo de operações diário (10). Tente de novo amanhã. !!!")

    elif numero_operacoes <=10:
        numero_operacoes += 1
        print("\n================ EXTRATO ================")
        print("\n Não foram realizadas movimentações ainda.\n" if not extrato else extrato)
        print(f"\nSaldo em {data_operacao}:\tR$ {saldo:.2f}")
        print("==========================================")

    return data_ultima_operacao, numero_operacoes


def criar_usuario(usuarios):

    cpf = input("Informe o CPF do cliente (somente números): ")


    if [usuario for usuario in usuarios if usuario["cpf"] == cpf]:
        print("\n!!! Já existe cliente com esse CPF! !!!")
        return

    nome = input("Informe o nome completo do novo cliente: ")
    data_nascimento = input("Informe a data de nascimento no formato (dd-mm-aaaa): ")
    endereco = input("Informe o endereço no formato (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("+++ Cliente criado com sucesso! +++")



def criar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF do cliente: ")
    usuario = [usuario['nome'] for usuario in usuarios if usuario["cpf"] == cpf]
    
    if usuario:
        print("\n+++ Conta criada com sucesso! +++")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!! Usuário não encontrado, fluxo de criação de conta encerrado! !!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE_OPERACOES = 10

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_operacoes = 0
    usuarios = []
    contas = []
    data_hoje = date.today()
    data_operacao = data_hoje.strftime("%d/%m/%Y")
    data_extrato = data_hoje.strftime("%d/%m/%Y %H:%M")
    data_ultimo_saque = ""
    data_ultima_operacao = ""

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato, numero_operacoes, data_ultima_operacao = depositar(saldo, valor, extrato, data_operacao, data_extrato, data_ultima_operacao, numero_operacoes)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_operacoes, data_ultima_operacao, data_ultimo_saque, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                numero_operacoes = numero_operacoes, 
                data_operacao = data_operacao, 
                data_ultimo_saque = data_ultimo_saque, 
                data_extrato = data_extrato, 
                data_ultima_operacao = data_ultima_operacao
            )

        elif opcao == "e":
            data_ultima_operacao, numero_operacoes = exibir_extrato(saldo, data_ultima_operacao, data_operacao, extrato=extrato, numero_operacoes = numero_operacoes)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("!!! Operação inválida, por favor selecione novamente a operação desejada. !!!")


main()
