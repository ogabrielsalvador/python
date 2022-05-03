
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).upper().split()

n1 = str(cidade[0] == 'SANTO')
n2 = n1.replace('True', 'começa')
n3 = n2.replace('False', 'não começa')

print(f'O nome da cidade em que você nasceu {n3} com Santo')
