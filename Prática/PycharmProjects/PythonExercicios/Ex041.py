
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima de 25 anos: MASTER

from datetime import date

ano_atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento? '))

idade = ano_atual - nascimento

if idade < 10:
    print(f'O atleta tem {idade} anos. \nClassificação: MIRIM')
elif idade < 15:
    print(f'O atleta tem {idade} anos. \nClassificação: INFANTIL')
elif idade < 20:
    print(f'O atleta tem {idade} anos. \nClassificação: JÚNIOR')
elif idade < 26:
    print(f'O atleta tem {idade} anos. \nClassificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos. \nClassificação: MASTER')
