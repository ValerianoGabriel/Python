'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''

while True:
    try:
        numero = int(input('Digite um número: '))
    except ValueError:
        print('Apenas número são permitidos no campo acima')
        numero = int(input('Digite um número: '))

    for ele in range(0, 11):
        print(f'{numero} x {ele} = {numero * ele}')

    escolha = input('Deseja continuar? [S/N]').strip().upper()

    if escolha == 'S':
        numero = int(input('Digite um número: '))
        for ele in range(0, 11):
            print(f'{numero} x {ele} = {numero * ele}')

    else:
        print('Até mais!')
        break

