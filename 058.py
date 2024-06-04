'''
Crie um programa onde serão informados diversos valores em uma lista. Caso o número já exista ele não será adicionado.
No final, serão exibidos todos os valores únicos em ordem crescente
'''

lista = [10, 20, 30, 40, 50, 60]


while True:
    try:
        numero = int(input('Digite um número: '))
    except ValueError:
        print('Apenas números são permitidos')
        numero = int(input('Digite um número: '))

    if numero in lista:
        print('Número já está na lista')
    else:
        lista.append(numero)
        print(lista)

