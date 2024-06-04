'''
Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10,
entre 10 e 20 ou maior que 20.
'''
from funcoes import saudacoes

saudacoes()

while True:
   try:
      numero = int(input('Digite um número: '))
   except ValueError:
      print('Digite apenas números.')
      numero = int(input('Digite um número: '))

   if numero <= 10:
      print('Número está entre 0 e 10 ')
   elif numero > 10 and numero <= 20:
      print('Número está entre 10 e 20')
   elif numero > 20:
      print('Número é maior que 20')
   else:
      print('Menor que 0')