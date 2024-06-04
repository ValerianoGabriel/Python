'''
Escreva um programa que converta real para o Franco Congolês
'''
from funcoes import saudacoes

saudacoes()

while True:
    #Leitura de variável
    try:
        real = float(input('Informe o valor em real: '))
        franco = real * 560

        #Taxa de cambio
        print(f'{real:.2f} reais equivalem a {franco:.2f} Francos Congoleses ')

    except ValueError:
        print('O valor deve ser informado em forma de número. Por favor, digite novamente.')
