'''
Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:

Quantas pessoas foram cadastradas
Uma listagem com as pessoas com o maior QI
Uma listagem com as pessoas de menor QI
'''
from funcoes import saudacoes

saudacoes()

pessoas = []
qi = []

while True:
    pessoas = input('Digite o seu nome: ')
    qi = input('Digite o seu QI: ')
    pergunta = input('Deseja continuar? [S/N]: ').upper()

    if pergunta == 'N':
        pessoas.append(pessoas)
        qi.append(QI)
        break
        print(enumerate(pessoas))
        print(min(QI))
        print(max(QI))
