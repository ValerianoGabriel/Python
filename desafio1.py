'''
Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário


Saída esperada:

A posição do objeto no tempo x é de y (m)

S = S0 + V0.t  + a.t2/2
'''

#ENTRADA DOS DADOS
posicao_inicial = float(input('Digite a posição inicial: '))
velocidade_inicial = float(input('Digite a velocidade inicial: '))
tempo = float(input('Digite o tempo: '))
aceleracao = float(input('Digite a aceleração: '))


#CÁLCULO
posicao = posicao_inicial + (velocidade_inicial * tempo) + ((aceleracao + (tempo ** 2) / 2))

print(f'A posição do objeto no tempo {tempo:.2f} é de {posicao} (m)')