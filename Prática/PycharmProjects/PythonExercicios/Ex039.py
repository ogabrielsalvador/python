
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento: '))

idade = ano_atual - nascimento

if idade == 18:
    print('Você precisa se alistar esse ano')
elif idade < 18:
    tempo = 18 - idade
    print(f'Você precisa se alistar daqui {tempo} ano(s)')
else:
    tempo = idade - 18
    print(f'Faz {tempo} ano(s) que o seu tempo de alistamento passou')
