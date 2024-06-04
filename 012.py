'''
Crie um programa que leia um nome, e mostre o primeiro e o último nome

'''
from funcoes import saudacoes

saudacoes()

nome = input('Digite seu nome completo: ').split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')

#EXEMPLO QUE EU ADICIONEI AO EXERCÍCIO
print(f'Olá, {nome[0]} {nome[-1]}!')

#CORREÇÃO
'''
Nome_completo = input('Digite seu nome completo: ').strip()
Nome_completo = Nome_completo.split()
print(f'Primeiro nome: {Nome_completo[0]}')
print(f'Primeiro nome: {Nome_completo[len(Nome_completo) - 1]}')
print(f'Último nome: {Nome_completo[-1]}')
'''




