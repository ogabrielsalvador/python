
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no
# final do jogo.

from random import randint

print('{}=\n  JOGO DO PAR OU ÍMPAR'.format('=-' * 12))

c = 0
while True:
    print('{}='.format('=-' * 12))
    maquina = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    soma = maquina + jogador
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper()
    while opcao != 'P' and opcao != 'I':
        opcao = str(input('Par ou Ímpar? [P/I] ')).upper()
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {maquina}. Total de {soma} DEU PAR')
    else:
        print(f'Você jogou {jogador} e o computador jogou {maquina}. Total de {soma} DEU ÍMPAR')
    if opcao == 'P' and soma % 2 != 0 or opcao == 'I' and soma % 2 == 0:
        break
    c += 1
    print('{}\nVocê VENCEU!\nVamos jogar novamente...'.format('-' * 25))
print('{}\nVocê PERDEU!'.format('-' * 25))
print(f'GAME OVER! Você venceu {c} vezes seguidas')
