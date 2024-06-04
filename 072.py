'''
Crie um programa que leia o nome, sexo e idade de vários Alunos, guardando os dados de cada aluno
em um dicionário e todos os dicionários em uma lista. No final mostre:

Quantas pessoas foram cadastradas
A média de idade do grupo
Uma lista com todas as mulheres
Uma lista com todas as pessoas com idade acima da média
'''
from funcoes import saudacoes, joinha

saudacoes()

alunos = []  # Alterei para uma lista para armazenar múltiplos alunos

while True:
    nome = input('Digite o nome do aluno [Digite FIM para sair]: ').strip().upper()
    if nome == 'FIM':
        break
    sexo = input('Digite seu sexo [M/F]: ').upper()
    idade = int(input('Digite sua idade: '))

    # Adicionando os dados do aluno em um dicionário
    aluno = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    alunos.append(aluno)  # Adicionando o dicionário à lista de alunos

print('-' * 30)

total_alunos = len(alunos)
soma_idades = sum(aluno['Idade'] for aluno in alunos)
media_idade = soma_idades / total_alunos

mulheres = [aluno['Nome'] for aluno in alunos if aluno['Sexo'] == 'F']
acima_da_media = [aluno['Nome'] for aluno in alunos if aluno['Idade'] > media_idade]

print(f'Total de alunos cadastrados: {total_alunos}')
print(f'Média de idade do grupo: {media_idade:.2f}')
print(f'Lista de mulheres: {", ".join(mulheres)}')
print(f'Lista de pessoas com idade acima da média: {", ".join(acima_da_media)}')
