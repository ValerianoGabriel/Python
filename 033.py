#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500
soma = 0
for ele in range(0, 501):
     if ele % 4 == 0:
        print(ele)
        soma = ele +soma
print(f'A soma dos números múltiplos de 4 é: {soma}')

#ALTERNATIVA
'''
soma = 0
for ele in range(1, 501):
     if ele % 4 == 0:
        print(ele)
        soma += ele
print(f'A soma dos números múltiplos de 4 é: {soma}')
'''