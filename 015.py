'''
Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar
'''
from funcoes import saudacoes

saudacoes()

while True:
    try:
        numero = float(input('Digite um número: '))
        if numero % 2 == 0:
            print('O número é par')
        else:
            print('O número é ímpar')

    except ValueError:
        print('Apenas números são válidos para este campo. Por favor, tente novamente.')


