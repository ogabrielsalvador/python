
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    par.append(n) if n % 2 == 0 else impar.append(n)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print(f'A lista completa é {sorted(lista)}\nA lista de pares é {sorted(par)}\nA lista de ímpares é {sorted(impar)}')
