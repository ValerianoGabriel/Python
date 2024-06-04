#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos


for ele in range(1 ,8):
    peso = float(input(f'Digite o {ele} peso: '))

    if ele == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'O maior peso é {maior}'
      f'\nO menor peso é {menor}')


