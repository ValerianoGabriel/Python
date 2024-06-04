'''
Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função


Exemplo:
       ----------------------------
            Senai Show de bola
       ----------------------------
'''

from funcoes import saudacoes

saudacoes()

def mensagem(msg):
    print('---' + '-' * len(msg) + '---')
    print(' ' * 3 + msg + ' ' * 3)
    print('---' + '-' * len(msg) + '---')

msg = input('Digite uma frase aqui: ').strip()
mensagem(msg)