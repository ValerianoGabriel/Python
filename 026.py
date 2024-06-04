'''
Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
 IMC = peso/(altura x altura)

 IMC abaixo de 18,5: Abaixo do peso
IMC entre 18,5 e 24,9: Peso normal
IMC entre 25 e 29,9: Sobrepeso
IMC acima de 30: Obesidade
'''
from funcoes import saudacoes

saudacoes()


while True:
    try:
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura (ex: 1.70): '))

        imc = peso / (altura * altura)

        linhas()

        if imc < 18.5:
            print('Abaixo do peso'
                  f'\nO seu IMC é: {imc:.2f}')
        elif imc >= 18.5 and imc < 24.9:
            print('Peso normal'
                  f'\nO seu IMC é: {imc:.2f}')
        elif imc >= 25 and imc < 29.9:
            print('Sobrepeso'
                  f'\nO seu IMC é: {imc:.2f}')
        elif imc >= 30:
            print('Obesidade'
                  f'\nO seu IMC é: {imc:.2f}')
        else:
            print('Erro')
        linhas()
    except ValueError:
        print('Apenas números são permitidos. Por favor, tente novamente')