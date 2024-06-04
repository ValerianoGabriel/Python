'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''


soma = 0
contagem = 0

while True:
    numero = input('Digite um número: ').strip()
    if numero == '0000':
        break

    soma += int(numero)
    contagem += 1

print(f'Temos {contagem} números'
      f'\nA soma é {soma}')


