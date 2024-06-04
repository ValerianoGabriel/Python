'''
Crie um programa para jogar JOKEMPO, usando a função random.randint
'''

import random
import time

def linhas():
    print('-' * 30)

'''
aleatorio = int(input('Escolha um número de 1 a 3: '))
aleatorio = random.randint(1,3)

if aleatorio == 1:
    print('Você escolheu pedra')
elif aleatorio == 2:
    print('Você escolheu tesoura')
elif aleatorio == 3:
    print('Você escolheu papel')
else:
    print('Erro')
'''

#CORREÇÃO
print('Bem-vindo ao JOKEMPO DA SORTE')

while True:
    pc = random.randint(1, 3)
    try:
        jogador = int(input('[1. Pedra]'
                        '\n[2. Papel]'
                        '\n[3. Tesoura]'
                        '\nDigite a sua escolha: '))

        time.sleep(0.5)
        print('Jo')
        time.sleep(0.5)
        print('Kem')
        time.sleep(0.5)
        print('Po!')
        time.sleep(0.5)

        linhas()

        if pc == jogador:
            print('Empate')
            linhas()

        elif jogador == 1 and pc == 3:
            print('Você ganhou!' 
                  '\nPedra x Tesoura')
            linhas()
        elif jogador == 2 and pc == 1:
            print('Você ganhou!' 
                  '\nPedra x Tesoura')
            linhas()
        elif jogador == 3 and pc == 2:
            print('Você ganhou!' 
                  '\nPedra x Tesoura')
            linhas()

        elif pc == 1 and jogador == 3:
            print('Você perdeu!' 
                  '\nPedra x Tesoura')
            linhas()
        elif pc == 2 and jogador == 1:
            print('Você perdeu!' 
                  '\nPedra x Tesoura')
            linhas()
        elif pc == 3 and jogador == 2:
            print('Você perdeu!' 
                  '\nPedra x Tesoura')
            linhas()
        else:
            print('Erro! O número informado não consta nas escolhas')
            linhas()
    except ValueError:
        print('Digite apenas números para uma melhor experiência e mais facilidade')

