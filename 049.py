'''
Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno
'''

def area(largura, comprimento):
    resultado = largura * comprimento
    return resultado

largura = int(input('Informe a largura do muro: '))
comprimento = int(input('Informe o comprimento do muro: '))
print(f'{area(largura, comprimento)}m²')