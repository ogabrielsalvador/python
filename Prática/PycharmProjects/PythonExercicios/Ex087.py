
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
soma_par = soma_coluna3 = 0
maior_linha2 = 0

for i in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {c}]: '))
        matriz[i].append(n)
        if n % 2 == 0:                          # item A
            soma_par += n
        if c == 2:                              # item B
            soma_coluna3 += n
        if i == 1:                              # item C
            if c == 0:
                maior_linha2 = n
            elif n > maior_linha2:
                maior_linha2 = n

print('=' * 32)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[i][c]:^3} ]', end='')
    print('')
print('=' * 32)

print(f"A soma dos valores pares é {soma_par} \nA soma dos valores da terceira coluna é {soma_coluna3} \n"
      f"O maior valor da segunda linha é {maior_linha2}")
