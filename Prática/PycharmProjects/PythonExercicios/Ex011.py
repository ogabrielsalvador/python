
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Qual a largura em metros da parede? '))
altura = float(input('Qual a altura em metros da parede? '))

area = largura * altura
rend = area / 2

print('A área total da parede é de {:.2f} m² \nPortanto será necessário {:.2f} litros de tinta'.format(area, rend))
