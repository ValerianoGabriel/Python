'''
Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
'''
import random

numero_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
                  'Treze','Quatorze', 'Quinze')


numeros = int(input('Digite um número: '))
print(numero_extenso[numeros])