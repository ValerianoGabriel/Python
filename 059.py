'''
Faça um programa com uma função maior e menor, que leia uma lista com 5 valores informados pelo usuário e
retorne esses valores e a posição deles

'''
from funcoes import saudacoes

saudacoes()
def maior(lista):
    maiorValor = max(lista)
    return maiorValor, lista.index(maiorValor)

def menor(lista):
    menorValor = min(lista)
    return menorValor, lista.index(menorValor)
lista = []

for numero in range(5):
    num = int(input('Digite um número: '))
    lista.append(num)

print(lista)
print('Menor: ', menor(lista))
print('Maior:', maior(lista))



