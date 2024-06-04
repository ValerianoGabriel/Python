'''
Crie uma função para verificar se um número é par ou ímpar
'''
def impopa(numero):
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')

while True:
        numero = float(input('Digite um número: '))
        impopa(numero)
        pergunta = input('Deseja continuar? [S/N] -> ').strip().upper()


        if pergunta == 'N':
            print('Até mais!')
            break
        else:
                numero = float(input('Digite um número: '))
                impopa(numero)
                pergunta = input('Deseja continuar? [S/N] -> ').strip().upper()