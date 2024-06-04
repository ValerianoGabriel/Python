'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²

Volume da Esfera: Y
Área da esfera: X

'''
from funcoes import saudacoes

saudacoes()

while True:
    try:
        raio = float(input('Informe o valor do raio(m): '))
        area = 4 * 3.1415 * raio ** 2
        volume = (4/3) * 3.1415 * raio ** 3
        print(f'Volume da Esfera: {volume:.2f} m³ \nÁrea da esfera: {area:.2f} m²')
    except ValueError:
        print('O valor do raio deve ser um número. Por favor, digite novamente')
