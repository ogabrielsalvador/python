
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados iguais, um diferente - ESCALENO: todos os lados diferentes

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if n1 == n2 == n3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
