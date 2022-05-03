
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar; [ 2 ] multiplicar; [ 3 ] maior; [ 4 ] novos números; [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 == n2:
            print(f'Os números são iguais, portanto não há número maior entre eles')
        elif n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('', end='')
    else:
        print('A opção selecionada é inválida. Por favor, tente novamente...')
    print('=-=' * 15)

print('\nFinalizando', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.7)
print('.', end=' ')
sleep(0.9)
print('.')
sleep(1)
print('{}\nFim do programa! Volte sempre!'.format(' '))
