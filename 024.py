'''
Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").
'''
from funcoes import saudacoes

saudacoes()

while True:
    senha = input('Digite vossa senha: ')
    if senha == 'python123':
        print('Senha correta')
        break
    else:
        print('Senha incorreta!')