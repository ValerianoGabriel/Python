'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
Ao final deve mostrar a quantidade de vitórias
'''

import random
import time

vitorias = 0

print('--- Bem-vindo! ---')

while True:
    pc = random.randint(1, 10)

    escolha = int(input('Digite'
                        '\n1 - Par'
                        '\n2 - ímpar: '))
    jogada = int(input('Qual a sua jogada?: '))

    time.sleep(0.5)
    print('Ímpar')
    time.sleep(0.5)
    print('ou')
    time.sleep(0.5)
    print('Par')
    time.sleep(0.5)

    if (pc +jogada) % 2 == 0 and escolha == 1 \
            or ((pc + jogada) % 2 == 1 and escolha == 2):
        print('Você ganhou! :)')
        vitorias += 1

    else:
        print(f'Você perdeu!')
        print(f'A soma é {pc + jogada} e você ganhou {vitorias}x')


    break