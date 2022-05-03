
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
# vencer

from random import randint

maquina = randint(0, 10)

print('{}\n{}\n{} JOGO DE ADIVINHAÇÃO {}\n{}'.format(' ', '=' * 22, '\033[1;36m', '\033[m', '=' * 22))
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')

jogador = int(input('Qual é seu palpite? '))
c = 1

while jogador != maquina:
    while jogador < maquina:
        print('Mais... Tente mais uma vez')
        jogador = int(input('Qual é seu palpite? '))
        c += 1
    while jogador > maquina:
        print('Menos... Tente mais uma vez')
        jogador = int(input('Qual é seu palpite? '))
        c += 1

print('{}\n{}VOCÊ ACERTOU!{}\nO número que eu pensei foi o {} e você precisou de {} tentativas para acertar.'
      .format(' ', '\033[1;32m', '\033[m', maquina, c))
