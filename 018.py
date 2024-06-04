'''
Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).
'''
from funcoes import saudacoes

saudacoes()

while True:
   try:
      idade = int(input('Digite sua idade: '))
   except ValueError:
      print('A idade precisa ser informada com números. Por favor, tente novamente')
      idade = int(input('Digite sua idade: '))

   if idade >= 60:
      print('Você é idoso')


   elif idade >= 18:
      print('Você é maior de idade')


   else:
      print('Você é menor de idade')