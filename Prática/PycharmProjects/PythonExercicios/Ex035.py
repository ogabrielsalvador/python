
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULO')
print('-=-' * 15)

a1 = float(input('Informe o comprimento da primeira reta: '))
a2 = float(input('Informe o comprimento da segunda reta: '))
a3 = float(input('Informe o comprimento da terceira reta: '))

if a1+a2 > a3 and a1+a3 > a2 and a2+a3 > a1:
    print(f'Essas retas PODEM FORMAR um triângulo')
else:
    print(f'Essas retas NÃO PODEM FORMAR um triângulo')
