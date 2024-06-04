'''
Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital, população e idioma oficial. 
Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.
'''
paises = {'Letônia': ['Riga', '1,884 milhão', 'Letão'],
          'Uzbequistão': ['Toshkent', '34,92 milhões', 'Uzbeque'],
          'Paquistão': ['Islamabade', '231,4 milhões', 'Urdu'],
          'Guiné Bissau': ['Bissau', '2,061 milhões', 'Português'],
          'Turcomenistão': ['Asgabate', '6,342 milhões', 'Turcomeno']}


while True:
    escolha = input('Digite o nome do país: ')
    if escolha == 'Letônia':
        print(paises['Letônia'])
    elif escolha == 'Uzbequistão':
        print(paises['Uzbequistão'])
    elif escolha == 'Paquistão':
        print(paises['Paquistão'])
    elif escolha == 'Guiné Bissau':
        print(paises['Guiné Bissau'])
    elif escolha == 'Turcomenistão':
        print(paises['Turcomenistão'])
    else:
        print('Erro')
