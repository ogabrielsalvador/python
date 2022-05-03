
#  Faça um programa que tenha uma função chamada área(),
#  que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def titulo(msg):
    print(f'{"-" * (len(msg) + 4)}\n  {msg}  \n{"-" * (len(msg) + 4)}')


def area(largura, comprimento):
    print(f'As dimensões do terreno são de {largura:.2f} x {comprimento:.2f} m. '
          f'Tendo uma área total de {largura * comprimento}m².')


titulo('CALCULADORA DE ÁREA')
larg = float(input('Largura: [em metros] '))
compr = float(input('Comprimento: [em metros] '))
area(larg, compr)
