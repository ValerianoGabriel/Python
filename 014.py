'''
Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.
'''
from funcoes import saudacoes

saudacoes()

while True:
    try:
        numero = float(input('Digite um número: '))
        if numero >= 0:
            print('O número é positivo')
        else:
            print('O número é negativo')

    except ValueError:
        print('Apenas números são permitidos neste campo. Por favor, digite novamente.')

