'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

adaptação:

'''

print('--- Bem-vindo ao Nubielk ---')

valor_saque = int(input('Digite o valor a ser sacado: '))

cedulas_50 = valor_saque // 50
valor_saque = valor_saque % 50

cedulas_20 = valor_saque // 20
valor_saque = valor_saque % 20

cedulas_10 = valor_saque // 10
valor_saque = valor_saque %10

cedulas_1 = valor_saque

print(f'A quantidade de notas é: '
      f'\n50: {cedulas_50}'
      f'\n20: {cedulas_20}'
      f'\n10: {cedulas_10}'
      f'\n1: {cedulas_1}')



