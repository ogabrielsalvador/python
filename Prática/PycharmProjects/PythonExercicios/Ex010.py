
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

brl = float(input('Quantos reais você possui? R$ '))

usd = brl / 3.27

print('Você consegue comprar {:.2f} dólares no total.'.format(usd))
