'''
Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário
'''
from funcoes import saudacoes

saudacoes()
while True:
    try:
    #Leitura do nome
        nome = str(input('Digite o seu nome: '))

        idade = int(input('Digite a sua idade: '))



        cidade= str(input('Digite o local onde nasceu: '))

        #Retorno para o usuário
        print(f'O meu nome é {nome}, tenho {idade} anos e nasci em {cidade}')
    except ValueError:
        print('A idade deve ser um número. Por favor, tente novamente')