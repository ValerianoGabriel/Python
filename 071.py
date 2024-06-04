from datetime import datetime
'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
em um dicionário, se por acaso a Carteira de trabalho for diferente de zero. 
O Dicionário receberá também o ano de contratação e o salário. 
Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar


dic_funcionario = dict()
funcionario = list()
data_atual = datetime.date.year


# ENTRADA DOS DADOS

while True:
    try:
        cart_trabalho = dic_funcionario['cart_trabalho'] = int(input('Digite a sua carteira de trabalho (digite 0 caso não tenha): '))
        if cart_trabalho != 0:
            nome = dic_funcionario['nome'] = input('Digite o seu nome: ')
            nascimento = dic_funcionario['nascimento'] = int(input('Digite o seu ANO de nascimento: '))
            idade = dic_funcionario['idade'] = 2024 - nascimento
            ano_contratacao = dic_funcionario[' ano_contratacao'] = input('Digite a data que foi contratado: ')
            salario = dic_funcionario['salario'] = float(input('Digite o seu salário: '))
            funcionario.append(dic_funcionario.copy())
            print(funcionario)
        else:
            print('Não é possível continuar se você não possui uma carteira de trabalho')
            break


    except ValueError:
        print('Erro. Por favor, tentar novamente.')
'''
funcionarios = []

while True:
    nome = input('Digite o nome do funcionário')