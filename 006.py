'''
Escreva um programa que leia 6 notas diferentes e faça a média do aluno


Saída esperada:

A sua média final é : 5
'''
from funcoes import saudacoes

saudacoes()

while True:
    try:
        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input('Informe a segunda nota: '))
        nota3 = float(input('Informe a terceira nota: '))
        nota4 = float(input('Informe a quarta nota: '))
        nota5 = float(input('Informe a quinta nota: '))
        nota6 = float(input('Informe a sexta nota: '))

        media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6

        print(f'A sua média final é : {media}')

    except ValueError:
        print('Os valores devem ser informados em forma de números. Por favor, digite novamente.')