
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastro = dict()

cadastro['Nome'] = str(input('Nome: ')).strip().title()
ano_atual = date.today().year
cadastro['Idade'] = ano_atual - int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('nº da CTPS [0 se não tiver]: '))

if cadastro['CTPS'] != 0:
    cadastro['Ano Contratação'] = int(input('Ano da primeira contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (35 - (ano_atual - cadastro['Ano Contratação']))
print(f'{"--==" * 10}--')

for k, v in cadastro.items():
    print(f'-> {k} tem o valor {v}')
