'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número.
E no final, retorne também a quantidade de tentativas necessárias.
'''

import random

print('Bem-vindo ao Jogo do adivinha')

pc = random.randint(1, 10)
jogador = None
tentativas = 0

while pc != jogador:
    jogador = int(input('Digite um número: '))
    if pc != jogador:
        print('Jogo do adivinha. Adivinha quem errou?')

    tentativas += 1
else:
    print('Acertou, campeão!'
        f'\nNúmero de tentativas até acertar foi: {tentativas}')
