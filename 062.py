'''
Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas listas.
Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].
'''
from funcoes import saudacoes


lista1 = [8, 7, 3, 5, 4, 9]
lista2 = [4, 5, 7, 3, 6, 8]
lista3 = []

for ele in range(0, len(lista1)):
    lista3.append(lista1[ele] + lista2[ele])

print(lista3)
