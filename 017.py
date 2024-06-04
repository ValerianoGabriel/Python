'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''
from funcoes import saudacoes

saudacoes()

while True:
    letra = input('Digite uma letra: ').lower()

    if letra in 'aeiou':
      print('A letra é Vogal')

    elif letra in '1234567890':
        print('O dado informado é um número')
    else:
       print('A letra é Consoante')
