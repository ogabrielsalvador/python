
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar; [ 2 ] multiplicar; [ 3 ] maior; [ 4 ] novos números; [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
opcao = str(input('>>>>> Qual é a sua opção? '))

while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
    print('A opção selecionada é inválida. Por favor, tente novamente...\n{}'.format('=-=' * 20))
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = str(input('Qual é a sua opção? '))

while opcao != '5':
    while opcao == '1':
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
        print('{}\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'
              .format('=-=' * 20))
        opcao = str(input('Qual é a sua opção? '))
    while opcao == '2':
        produto = n1 * n2
        print(f'O produto entre {n1} x {n2} é {produto}')
        print('{}\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'
              .format('=-=' * 20))
        opcao = str(input('Qual é a sua opção? '))
    while opcao == '3':
        if n1 == n2:
            print(f'Os números são iguais, portanto não há número maior entre eles')
        elif n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
        print('{}\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'
              .format('=-=' * 20))
        opcao = str(input('Qual é a sua opção? '))
    while opcao == '4':
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('{}\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'
              .format('=-=' * 20))
        opcao = str(input('Qual é a sua opção? '))

print('Finalizando', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.7)
print('.', end=' ')
sleep(0.9)
print('.')
sleep(1)
print('{}\n{}\nFim do programa! Volte sempre!'.format('=-=' * 20, ' '))
