
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada

n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O número digitado foi {}. \nO seu dobro é {} \nO seu triplo é {}.'.format(n, dobro, triplo))
print('A sua raíz quadrada é {:.2f}.'.format(raiz))
