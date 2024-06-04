'''
Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos.
Em seguida, exiba o produto mais barato e o mais caro.
'''

produtos = {
    "Celta": 100000,
    "Palio": 27000,
    "Corsa": 25000,
    "Siena": 28000,
    "Voyage": 30000
}

valores = produtos.values()
maior = max(valores)
menor = min(valores)

print(f'O produto com maior valor é {menor[:]}')
print(f'O produto com menor valor é {maior[:]}')



