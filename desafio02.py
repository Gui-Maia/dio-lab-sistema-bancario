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
limite_saques = 3
numero_operacoes = 0
limite_operacoes = 10

data_hoje = date.today()
data_operacao = data_hoje.strftime("%d/%m/%Y")
data_extrato = data_hoje.strftime("%d/%m/%Y %H:%M")
data_ultimo_saque = ""
data_ultima_operacao = ""

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0 and data_ultima_operacao != data_operacao:
            data_ultima_operacao = data_operacao
            numero_operacoes = 0
            saldo += valor
            extrato += f"{data_operacao} Depósito: R$ {valor:.2f}\n"
            numero_operacoes += 1    
        
        elif valor > 0 and numero_operacoes <= 10:
            saldo += valor
            extrato += f"{data_operacao} Depósito: R$ {valor:.2f}\n"
            numero_operacoes += 1

        elif numero_operacoes > 10:
            print("Você atingiu o limite máximo de operações diário (10). Tente de novo amanhã.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_operacoes > 10:
            print("Você atingiu o limite máximo de operações diário (10). Tente de novo amanhã.")

        elif numero_saques >= limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0 and data_hoje == data_ultimo_saque:
            saldo -= valor
            extrato += f"{data_extrato} Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            if data_ultima_operacao != data_operacao:
                data_ultima_operacao = data_operacao
                numero_operacoes = 0

            numero_operacoes += 1
        
        elif valor > 0 and data_hoje != data_ultimo_saque:
            saldo -= valor
            extrato += f"{data_extrato} Saque: R$ {valor:.2f}\n"
            numero_saques = 1

            if data_ultima_operacao != data_operacao:
                data_ultima_operacao = data_operacao
                numero_operacoes = 0
            
            numero_operacoes += 1
            data_ultimo_saque = data_hoje

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":

        if data_ultima_operacao != data_operacao:
            data_ultima_operacao = data_operacao
            numero_operacoes = 0
            print("\n================ EXTRATO ================")
            print("\n Não foram realizadas movimentações ainda.\n" if not extrato else extrato)
            print(f"\nSaldo em {data_operacao}: R$ {saldo:.2f}")
            print("==========================================")
            numero_operacoes += 1
        
        elif numero_operacoes > 10:
            print("Você atingiu o limite máximo de operações diário (10). Tente de novo amanhã.")

        elif numero_operacoes <=10:
            numero_operacoes += 1
            print("\n================ EXTRATO ================")
            print("\n Não foram realizadas movimentações ainda.\n" if not extrato else extrato)
            print(f"\nSaldo em {data_operacao}: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente uma operação válida.")
