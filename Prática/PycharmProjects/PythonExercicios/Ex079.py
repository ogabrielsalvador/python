
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
c = 1

while True:
    n = int(input(f'Digite o {c}º valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        c += 1
        print('Valor adicionado com sucesso...')
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print('\nOs valores digitados e adicionados foram:', end=' ')
for n in sorted(lista):
    print(n, end=' ')
print('')
