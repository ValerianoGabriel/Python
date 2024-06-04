'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,

1. mostre a média entre todos os valores
2. qual foi o maior e o menor valores lidos.
3. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

'''

escolha = ''

while escolha != 'N':
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    n4 = int(input('Digite um número: '))

    print(f'A média é: {(n1 + n2 +n3 + n4)/4}'
         f'\nO maior valor informado é {max(n1, n2, n3, n4)}'
         f'\nO menor valor informado é {min(n1, n2, n3, n4)}')


    escolha = (input('Deseja continuar? [S/N]').upper())


print('Obrigado!')
