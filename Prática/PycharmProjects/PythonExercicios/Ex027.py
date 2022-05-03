
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).title().split()

# o 'len' vai contar qts palavras a lista possui, 'Ana Paula de Matos' possui 4 palavras, o '-1' é pq a numeração das
# palavras começa em 0, portanto 'lista[len(lista)-1] == lista[4-1] == lista [3] == Matos.

print(f'Muito prazer em te conhecer {nome[0]} {nome[len(nome)-1]}!')
print(f'Seu primeiro nome é: {nome[0]} \nSeu último nome é {nome[len(nome)-1]}')
