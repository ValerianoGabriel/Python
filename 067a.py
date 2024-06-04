'''
Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital, população e idioma oficial.
Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.
'''


paises = {
    'Letônia': {'capital': 'Riga', 'populacao': '1,884 milhão', 'idioma': 'Letão'},
    'Uzbequistão': {'capital': 'Toshkent', 'populacao': '34,92 milhões', 'idioma': 'Uzbeque'},
    'Paquistão': {'capital': 'Islamabade', 'populacao': '231,4 milhões', 'idioma': 'Urdu'},
    'Guiné Bissau': {'capital': 'Bissau', 'populacao': '2,061 milhões', 'idioma': 'Português'},
    'Turcomenistão': {'capital': 'Asgabate', 'populacao': '6,342 milhões', 'idioma': 'Turcomeno'}
}

pais_digitado = input("Digite o nome de um país: ")

if pais_digitado in paises:
    print(f"\nInformações sobre {pais_digitado}:")
    print("Capital:", paises[pais_digitado]['capital'])
    print("População:", paises[pais_digitado]['populacao'])
    print("Idioma Oficial:", paises[pais_digitado]['idioma'])
else:
    print("País não encontrado no dicionário.")