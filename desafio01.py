from datetime import date


menu = """
++++++++++++++++++++++++++++++++++++++++++

Escolha a operação bancária a ser feita

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

++++++++++++++++++++++++++++++++++++++++++
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
data_hoje = date.today()
data_operacao = data_hoje.strftime("%d/%m/%Y")
data_ultimo_saque = ""

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"{data_operacao} Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0 and data_hoje == data_ultimo_saque:
            saldo -= valor
            extrato += f"{data_operacao} Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        elif valor > 0 and data_hoje != data_ultimo_saque:
            saldo -= valor
            extrato += f"{data_operacao} Saque: R$ {valor:.2f}\n"
            numero_saques = 1
            data_ultimo_saque = data_hoje

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("\n Não foram realizadas movimentações ainda.\n" if not extrato else extrato)
        print(f"\nSaldo em {data_operacao}: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente uma operação válida.")
