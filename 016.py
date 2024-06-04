'''
Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.
'''
from funcoes import saudacoes

saudacoes()

while True:
   try:
      n1 = int(input('Digite o primeiro número: '))
      n2 = int(input('Digite o segundo número: '))
   except ValueError:
      print('Digite apenas números')
      n1 = int(input('Digite o primeiro número: '))
      n2 = int(input('Digite o segundo número: '))

   if n1 == n2:
      print('Os números são iguais')
   else:
      print('Os números são diferentes')
