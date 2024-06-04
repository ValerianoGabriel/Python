'''
Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

1. Apenas os 3 primeiros mais assistidos
2. Os últimos 2 mais assistidos
3. A lista em ordem alfabética
4. Em que posição está “O rei leão”

'''

def linhas():
    print('-' * 30)

print('Bem-vindo ao Cinema com Gabriel!')

linhas()

filmes = ('Avatar', 'Vingadores: Ultimato', 'Avatar: O Caminho da Água', 'Titanic',
          'Star Wars: Episódio VII - O Despertar da Força', 'Vingadores: Guerra Infinita',
          'Homem-Aranha: Sem Volta Para Casa', 'Jurassic World: O Mundo dos Dinossauros', 'O Rei Leão', 'Os Vingadores')

#1. Apenas os 3 primeiros mais assistidos
print('Os 3 mais assistidos da lista saaao:')
for count in range(0, 3):
    print(filmes[count])

linhas()

#2. Os últimos 2 mais assistidos
print('Os 2 menos assistidos da lista saaao:')
for count in range(8, 10):
    print(filmes[count])

linhas()

#3. A lista em ordem alfabética
print('Aqui estão os filmes separados por ordem alfabética:')
print(sorted(filmes))

linhas()

#4. Em que posição está “O rei leão”
print(filmes.index ('O Rei Leão') + 1)



