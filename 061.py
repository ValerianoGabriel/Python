'''
Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista
até que ele digite um número negativo.
Em seguida, exiba a lista na tela.

'''
from funcoes import joinha, linhas

joinha()
linhas()

lista = []

while True:
    try:
        numero = int(input('Digite um número (negativo para parar): '))
        if numero < 0:
            break
        lista.append(numero)
    except ValueError:
        print('Apenas números são permitidos.')


print(lista)
