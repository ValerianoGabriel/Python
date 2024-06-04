'''
Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.


Saída esperada:

O salário de 6000 com o reajuste de 60% será de : 9600

Fiz algumas alterações para que o usuário pudesse informar a porcentagem.
'''
from funcoes import saudacoes

saudacoes()

while True:
    try:
        salario = int(input('Informe o salário: '))
        porcentagem = int(input('Informe a porcentagem do reajuste: '))
        reajuste = 1 + (porcentagem/100)
        resultado = float(salario) * reajuste

        print(f'O salário de R${salario} com o reajuste de {porcentagem}% será de: R${resultado:.2f}')
    except ValueError:
        print('Por favor, insira apenas números.')