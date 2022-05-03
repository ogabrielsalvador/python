
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print(f'{"-" * 40}\n{"LISTAGEM DE PREÇOS":^40}\n{"-" * 40}')
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90)

for i in lista:
    if type(i) is str:
        print(f'{i:.<31}', end='')
    else:
        print(f'R${i:>7.2f}')
print('-' * 40)
