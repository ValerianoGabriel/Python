'''
Escreva um programa que crie um dicionário com as informações de 5 livros, como título, autor,
ano de lançamento e número de páginas. Em seguida, exiba apenas os autores dos livros.
'''

livros = {
    "títulos": [
        "1984",
        "To Kill a Mockingbird",
        "Harry Potter and the Philosopher's Stone",
        "The Great Gatsby",
        "The Catcher in the Rye"
    ],
    "autores": [
        "George Orwell",
        "Harper Lee",
        "J.K. Rowling",
        "F. Scott Fitzgerald",
        "J.D. Salinger"
    ],
    "anos_de_lançamento": [
        1949,
        1960,
        1997,
        1925,
        1951
    ],
    "números_de_páginas": [
        328,
        336,
        320,
        180,
        224
    ]
}


print(livros['autores'])
