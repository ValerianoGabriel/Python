#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta

#)
#(
#)(
#(()
#())
#()(
#()())
#()()(
from funcoes import saudacoes

saudacoes()

#Solicita que o usuário digite uma expressão com parenteses        print ('A expressão esta correta!')
expressao = input('Digite uma expressão com parênteses: ')

# Crie uma pilha vazia para armazenar os parênteses
pilha = []

#Percorre a expressão e verifica se os parênteses estão na ordem correta
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        try:
            if pilha [-1] == '(':
                pilha.pop()
            else:
                print('A expressão esta correta!')
                break
        except IndexError:
            print('A expressão esta incorreta!')
            break
else:
    if len(pilha) == 0:
        print ('A expressão esta correta!')
    else:
        print ('A expressão esta incorreta!')
