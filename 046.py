'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato

'''

escolha = ''

while True:
    produto = input('Digite o produto: ')
    preço = float(input('Digite o valor da camiseta: '))
    escolha = input('Deseja continuar? [S/N]').strip().upper()

    print(f'A média é: {produto}'
         f'\nO total de produtos com valor superior a R$1000 é  {preço > 1000}'
         f'\nO menor valor informado é {min(preco)}')




    break


