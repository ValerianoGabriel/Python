'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


Saída esperada:

A dobro de 9 é : 18
A triplo de 9 é : 27
A raiz quadrada de 9 é : 3

'''
from funcoes import saudacoes

saudacoes()

while True:
    try:
        numero = float(input('Informe um número: '))

        print(f'O dobro de {numero} é: {numero * 2}'
              f'\nO triplo de {numero} é: {numero * 3}'
              f'\nA raiz quadrada de {numero} é: {numero ** (1 / 2)}')

    except ValueError:
        print('Apenas números são permitidos. Por favor, tente novamente.')

