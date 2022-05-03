
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

a = float(input('Insira o valor do ângulo: '))

sen = sin(radians(a))
cos = cos(radians(a))
tag = tan(radians(a))

print('O ângulo informado foi o de {}º.\nO valor do SENO é {:.2f}.\nO valor do COSSENO é {:.2f}.\n'
      'O valor da TANGENTE é {:.2f}.'.format(a, sen, cos, tag))
