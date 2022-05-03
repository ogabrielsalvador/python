
# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'Os valores pares digitados foram: {sorted(numeros[0])}\nOs valores impares digitados foram: {sorted(numeros[1])}')
