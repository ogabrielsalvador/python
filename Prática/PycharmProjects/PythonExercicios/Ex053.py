
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).lower().split()
frase = ''.join(frase)
invertida = frase[::-1]

if frase == invertida:
    print('A frase digitada É UM PALÍNDROMO')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO')
