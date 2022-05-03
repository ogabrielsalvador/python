
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('{}\n Quer ver a tabuada de qual valor? '.format('=' * 35)))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c:2} x {n} = {n * c}')
        c += 1
