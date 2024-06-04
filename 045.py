'''
Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

'''

while True:
    numero = (input('Digite um número: '))

    if numero == '0000':
        print('Até mais!')
        break

    elif numero == '0':
        print('Tá de brincadeira né?!')
        break

    for ele in range(0 ,11):
        print(f'{numero} X {ele} = {int(numero) * ele}')
