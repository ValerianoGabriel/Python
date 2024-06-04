#Escreva um programa que verifique se uma palavra é um palíndromo.

palavra = input('Digite uma palavra: ').strip().lower()
palavra_invertida = palavra[::-1]


if palavra == palavra_invertida:
    print('É palíndromo')
else:
    print('Não é palíndromo')


