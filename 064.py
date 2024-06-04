'''
Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista,
que mantenha separado as consoantes das vogais
''''''
from funcoes import saudacoes

saudacoes()

def vogal(letra):
    Vogais = lista.index('aeiou')
    return letra in Vogais


lista = [[], []]

for _ in range(7):
    letras = input('Digite uma letra: ')
    lista.append(letras)

if vogais(lista) in letras:
    print(f'As vogais são {vogais(lista)} e as consoantes são {lista - vogais}')
else:
    print(lista)
'''
def vogal(letra):
    vogais = 'aeiouAEIOU'
    return letra in vogais

lista = {'vogais': [], 'consoantes': []}

for _ in range(7):
    letra = input('Digite uma letra: ')
    if vogal(letra):
        lista['vogais'].append(letra)
    else:
        lista['consoantes'].append(letra)

print(f'Vogais: {lista["vogais"]}')
print(f'Consoantes: {lista["consoantes"]}')
