'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
cadastrando tudo em uma lista composta
'''
from funcoes import linhas
import random
import time

lista = list()
jogos = list()
linhas()
quant = int(input('Quantos jogos serão gerados? '))
total = 1
linhas()
while total <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('E os números que lhe farão feliz sããão:')
linhas()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(0.7)
