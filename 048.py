'''
Crie um programa que pede ao usuário para digitar dois números e, em seguida, divida o primeiro número pelo segundo número.
No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido,
como uma string ou o número zero.
'''

while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        divisao = n1 / n2
        print(f'A divisão entre {n1} e {n2} é {divisao}')

    except ValueError:
        print('Isso lá é número?!')
        break

    except ZeroDivisionError:
        print('Erro: divisão por zero')
        break

