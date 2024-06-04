'''
Escreva um programa que leia o nome, e o sobrenome,
CONCATENE em uma nova variável nome completo, e retorne para o usuário
'''
from funcoes import saudacoes

saudacoes()

nome = str(input('Digite o seu nome: '))
sobrenome = str(input('Digite o seu sobrenome: '))

print(f'Seu nome completo é: {nome} {sobrenome}')

