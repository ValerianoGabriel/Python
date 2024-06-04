'''
Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
considerando a idade e os critérios de saúde.
'''

'''
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
horas_sono = int(input('Informe quantas horas dormiu de ontem para hoje: '))



if idade < 18 or idade > 60 or peso < 50 or horas_sono < 6:
   print('Infelizmente, você não pode doar sangue')
else:
   print('Você pode doar sangue!')

'''
from funcoes import saudacoes

saudacoes()

#CORREÇÃO
try:
   idade = int(input('Digite sua idade: '))
except ValueError:
   print('Digite apenas números, por favor.')
   idade = int(input('Digite sua idade: '))

if idade > 16 and idade < 60:
   try:
      peso = float(input('Digite seu peso: '))
   except ValueError:
      print('Por favor, digite apenas números')
      peso = float(input('Digite seu peso: '))


   if peso > 50 and peso < 140:
      documento = input('Tem os documentos[S/N]?: ').strip().lower()

      if documento[0] == 's':
         print('Pode doar')
      else:
         print('Não poderá doar, pois é necessário ter os documentos para doar sangue')

   else:
      print('Não poderá doar, pois o peso não está entre o adequado para doar sangue')

else:
   print('Não poderá doar, pois a idade não está entre a adequada para doar sangue')