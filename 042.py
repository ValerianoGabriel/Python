'''
Simulação de um Caixa Eletrônico. Este programa simula um caixa eletrônico, permitindo que o usuário faça

1. depósitos
2. saques
3. consulte o saldo da conta
4. sair

'''

print('--- Bem-vindo ao Nubielk ---')

saldo_atual = float(1000000)
saldo_poupanca = 0
escolha = ''
taxa = 0.01
while escolha != 7:
    print('---------------------------------')
    escolha = int(input('[1. Depositar]'
                        '\n[2. Sacar]'
                        '\n[3. Consultar Saldo]'
                        '\n[4. Empréstimo]'
                        '\n[5. Poupança]'
                        '\n[6. Consultar saldo poupança]'
                        '\n[7. Sair da Conta]'
                        '\nDigite a sua escolha: '))
    if escolha == 4 and escolha > 0:
        emprestimo = int(input('Digite o valor de empréstimo: '))
        if emprestimo < 0:
            print('Operação Inválida. Cód. do erro 171')
        else:
            print(f'O valor do emprestimo é R${emprestimo:.2f} e sua conta ficará com {saldo_atual + emprestimo:.2f}')
        saldo_atual += emprestimo



    elif escolha == 1 and escolha > 0:
        deposito = int(input('Digite o valor do depósito: '))
        if deposito < 0:
            print('Operação Inválida. Cód. do erro 171')
        else:
            deposito = int(input('Digite o valor do depósito: '))
            print(f'O valor do depósito é R${deposito:.2f} e sua conta ficará com {saldo_atual + deposito:.2f}')
            saldo_atual += deposito

    elif escolha == 2:
        saque = int(input('Digite o valor do saque: '))
        if saque < 0:
            print('Operação Inválida. Cód. do erro 171')
        else:
            print(f'O valor do saque é R${saque:.2f} e sua conta ficará com {saldo_atual - saque:.2f}')
        saldo_atual -= saque



    elif escolha == 5 and escolha > 0:
        poupança = int(input('Digite o valor para depositar na poupança: '))
        meses = int(input('Quantos meses pretende deixar rendendo? '))
        print(f'O valor do depósito na poupança é R${poupança:.2f} e sua poupança ficará com {saldo_poupanca + poupança:.2f}')
        print(f'O valor de {poupança} em {meses} meses lhe renderá R${(poupança * (1 + taxa) ** meses) - poupança:.2f}')
        saldo_poupanca += poupança
        saldo_atual = saldo_atual - saldo_poupanca
        print(f'O valor atual da sua conta corrente é {saldo_atual}')

    elif escolha == 6 and escolha > 0:
        print(f'O seu saldo atual da poupança é R${saldo_poupanca}')

    elif escolha == 3:
        print(f'O seu saldo atual é R${saldo_atual:.2f}')


    else:
        print('O Nubielk agradece a preferência!')
