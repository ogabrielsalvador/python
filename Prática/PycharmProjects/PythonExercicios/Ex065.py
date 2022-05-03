
# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

n = int(input('Digite um número: '))
opcao = str(input('Quer continuar? [S/N] ')).upper()

maior = n
menor = n
s = n
c = 1

while opcao != 'N':
    while opcao == 'S':
        n = int(input('Digite um número: '))
        s += n
        c += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao != 'S' and opcao != 'N':
        print('Opção digitada inválida. Por favor, tente novamente:')
        opcao = str(input('Quer continuar? [S/N] ')).upper()

print('Você digitou {} números e a média foi {:.2f}'.format(c, (s/c)))
print(f'O maior valor foi {maior} e o menor foi {menor}')
