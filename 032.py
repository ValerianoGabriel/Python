#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

try:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
except ValueError:
    print('Apenas números são permitidos. Por favor, recomece o processo.')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

for ele in range(n1, n2 + 1):
    if ele % 2 == 0:
        print(ele, end= ', ')

    elif n1 == n2:
        print('Os números informados são iguais.')

    else:
        print('Erro')