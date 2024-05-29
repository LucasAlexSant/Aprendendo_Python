print("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input("Digite a opção: ").lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Operação Negada! O valor é inválido.")

    elif opcao == 's':
        print(f"Saldo disponível: R${saldo:.2f}")
        valor = float(input("Informe o valor para o saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Negada! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação Negada! Valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação Negada! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R${valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Operação Negada! Valor inválido.")

    elif opcao == 'e':
        print("\nExtrato:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R${saldo:.2f}\n")

    elif opcao == 'q':
        print("Obrigado por usar o sistema bancário. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")