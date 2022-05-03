
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Qual é o seu nome completo? ')).upper().split()

n1 = str('SILVA' in nome)
n2 = n1.replace('True', 'possui')
n3 = n2.replace('False', 'não possui')

print(f'Você {n3} Silva no nome')
