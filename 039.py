# Faça um programa que leia um número e retorne o fatorial !
#
# 4! = 4 x 3 x 2 x 1

numero = int(input('Digite um número: '))
fatorial = 1
apoio = 1

while apoio != numero:
    apoio = apoio + 1
    fatorial = apoio * fatorial

print(f'{fatorial}')

#

