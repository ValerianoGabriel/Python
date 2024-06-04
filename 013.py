'''

Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez

'''
from funcoes import saudacoes

saudacoes()

frase = input('Digite uma frase aqui:').lower().strip()

print(f'A quantidade de As é: {frase.count("a")}'
      f'\nPrimeiro A: {frase.find("a") + 1}'
      f'\nÚltimo A: {frase.rfind("a") + 1}')


