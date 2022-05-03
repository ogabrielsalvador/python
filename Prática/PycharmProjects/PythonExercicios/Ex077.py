
#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON')

for p in palavras:          # ele passa a fazer o range de palavra por palavra, até chegar na última palavra listada.
    print(f'\nNa palavra {p.upper()} temos: ', end='')       # nesse caso o p representa a palavra selecionada na ordem.
    for letra in p:         # ele passa a fazer o range de letra por letra na palavra selecionada 'p'.
        if letra in 'AEIOU':        # se a letra selecionada estiver em 'AEIOU' irá ser feito o print dela.
            print(letra, end=' ')
