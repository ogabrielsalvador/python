
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

n = float(input('Qual a distância da viagem em Km? '))

if n <= 200:
    passagem = n * 0.5
else:
    passagem = n * 0.45

print('O valor da passagem é de R$ {:.2f}'.format(passagem))
