
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('A opção digitada não existe. TENTE NOVAMENTE!')
