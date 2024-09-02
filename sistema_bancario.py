saldo = 0
operacoes = []
qtd_saques = 0
VALOR_LIMITE_SAQUES = 500.00
QTD_LIMITE_SAQUES = 3

def menu():
    print(
          """
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [Q] Sair
          """
         )

def depositar():
    global saldo
    
    valor = float(input("Informe o valor do depósito: "))
    if valor >= 0:
        saldo += valor
        operacoes.append(f"Valor R$ {valor:.2f} inserido na conta!")
    else:
        print("Falha! Valor menor que zero não pode ser usado para depósito.")

def sacar():
    global qtd_saques
    global saldo

    valor = float(input("Informe o valor do saque: "))
    if (qtd_saques < QTD_LIMITE_SAQUES) and (valor <= VALOR_LIMITE_SAQUES):
        if saldo >= valor:
            if valor > 0:
                saldo -= valor
                operacoes.append(f"Valor {valor:.2f} sacado da conta!")
                qtd_saques += 1
            else:
                print("Falha! Informe um valor válido.")
        else:
            print("Falha! Não há saldo suficiente na conta. Não foi possível realizar a operação.")
    else:
        print(f"Falha! Valor maior que R$ {VALOR_LIMITE_SAQUES:.2f} ou limite de {QTD_LIMITE_SAQUES} saques excedido.")

def extrato():
    if len(operacoes) == 0:
        print("Não foram feitas operações na conta.")
    else:
        print(operacoes)
        print(f"Saldo: R$ {saldo:.2f}")

while True:
    menu()
    opcao = input("Informe a operação: ")

    if opcao == '1':
        depositar()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        extrato()
    elif opcao == 'q' or opcao == 'Q':
        break
    else:
        print("Operação inválida! Por favor, escolha novamente.")

print("Volte sempre!")