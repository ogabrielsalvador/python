
# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

hoje = date.today().year
contador = 0     # irá contar qts pessoas tem menos de 18

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if hoje - nasc < 18:
        contador += 1
print(f'Ao todo tivemos {7 - contador} pessoas maiores de idade \nE também tivemos {contador} pessoas menores de idade')
