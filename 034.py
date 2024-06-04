#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
soma = 0
for ele in range (0,10):
    try:
        numero =  int(input('Digite um número: '))
    except ValueError:
        print('Apenas números são permitidos. Recomece o processo.')
        numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        soma += numero

print(f'A soma dos pares é {soma}')