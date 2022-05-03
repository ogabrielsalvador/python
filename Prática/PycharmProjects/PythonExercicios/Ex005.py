
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor

n = int(input('Digite um número: '))

ant = n - 1
suc = n + 1

print('O número digitado foi {}, o seu sucessor é o {} e o seu antecessor é o {}'.format(n, suc, ant))

# Outra forma de fazer com o uso de menos variáveis
print('O número digitado foi {}, o seu sucessor é o {} e o seu antecessor é o {}'.format(n, (n+1), (n-1)))
