'''
Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele em três disciplinas:
matemática, português e história. Em seguida, exiba a média das notas do aluno.



num_alunos = int(input("Digite o número de alunos: "))

# Dicionário para armazenar as notas dos alunos
notas_alunos = {}

# Loop para ler as notas de cada aluno
for i in range(1, num_alunos + 1):
    nome_aluno = input(f"Digite o nome do aluno {i}: ")
    nota_matematica = float(input("Digite a nota de Matemática: "))
    nota_portugues = float(input("Digite a nota de Português: "))
    nota_historia = float(input("Digite a nota de História: "))

    # Adiciona as notas do aluno ao dicionário
    notas_alunos[nome_aluno] = {'Matemática': nota_matematica,
                                 'Português': nota_portugues,
                                 'História': nota_historia}

# Calcula e exibe a média das notas de cada aluno
print("\nMédia das notas dos alunos:")
for nome, notas in notas_alunos.items():
    media = sum(notas.values()) / len(notas)
    print(f"{nome}: {media:.2f}")
'''
from funcoes import saudacoes
alunos = {}

while True:
    nome = input('Digite o nome do aluno[Fim]: ').strip().title()
    if nome == 'Fim':
        break
    matematica = float(input('Digite a nota de matemática: '))
    historia = float(input('Digite a nota de historia: '))
    portugues = float(input('Digite a nota de portugues: '))

    alunos[nome] = {'Matemática': matematica, 'Historia': historia, 'Portugues': portugues}

print('-' * 30)

for nome, notas in alunos.items():
    print(f'A média de {nome} é : {sum(notas.values()) / len (notas.values())}')
