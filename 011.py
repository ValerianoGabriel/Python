'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras no geral (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''
from funcoes import saudacoes

saudacoes()

nome = input('Digite seu nome completo: ')
nome_separado = nome.split()
nome_sem_espacos = nome.replace(' ', '')
primeiro_nome = len((nome_separado[0]))

print(nome.upper())
print(nome.lower())
print(len(nome_sem_espacos))
print(primeiro_nome)


#ALTERNATIVA
'''
Nome = input('Digite o seu nome completo: ').strip()
print(f'Seu nome em maiusculo é {Nome.upper()}')
print(f'Seu nome em maiusculo é {Nome.lower()}')

#Contar quantos espaços tem
quant_espacos = Nome.count(' ')
print(f'A quantidade de letras é {len(Nome) - quant_espacos}')
print(f'A quantidade de letras é {len(Nome.replace(" ", " "))}')

#Quantidade 1 nome
print(f'A quantidade de letras é {len(Nome.split()[0])}')
'''




