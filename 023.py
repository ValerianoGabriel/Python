'''
Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.
'''
from funcoes import saudacoes

saudacoes()

palavra = input('Digite uma palavra: ').strip().lower()

if palavra[0] in 'aeiou':
    print('Começa com vogal')
else:
    print('Começa com consoante')
