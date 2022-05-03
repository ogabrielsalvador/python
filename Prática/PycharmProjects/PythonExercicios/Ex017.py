
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa

from math import hypot

ca = float(input('Insira o comprimento do cateto adjacente: '))
co = float(input('Insira o comprimento do cateto oposto: '))

hip1 = pow(pow(ca, 2) + pow(co, 2), 1/2)

# Também posso calcular da seguinte forma:

hip2 = (ca ** 2 + co ** 2) ** (1/2)

print('O comprimento da hipotenusa é igual a {:.2f}.'.format(hip1))
print('O comprimento da hipotenusa é igual a {:.2f}.'.format(hip2))

# Com o uso da importação de Ex107 (math)

hip3 = hypot(ca, co)

print('O comprimento da hipotenusa é igual a {:.2f}.'.format(hip3))
