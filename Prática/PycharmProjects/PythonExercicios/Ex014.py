
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

tc = float(input('Digite a temperatura em Celsius: '))

tf = (tc * 1.8) + 32

print('A temperatura em Fahrenheit é de {:.2f}ºF'.format(tf))
