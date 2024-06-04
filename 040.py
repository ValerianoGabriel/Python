# Escreva um programa que leia um número n inteiro qualquer e
# mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

# F(n)=F(n−1)+F(n−2)

numero = int(input('Digite um número inteiro: '))

fatorial = ''
apoio = ''

while apoio != numero:
    apoio = numero - 1
    fatorial = numero - 2

print(f'{fatorial}')

