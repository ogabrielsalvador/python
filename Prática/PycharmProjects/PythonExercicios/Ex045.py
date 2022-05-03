
# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
import pygame

print('{}{}{} VAMOS JOGAR JOKENPO?!! {}{}{}'.format('\033[1;33m', '='*20, '\033[1;31m', '\033[1;33m', '='*20, '\033[m'))
print('Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = int(randint(0, 2))
jogador = int(input('Qual é a sua jogada? '))

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Ex045.mp3')
pygame.mixer.music.play()
print('JO')
sleep(0.4)
print('KEN')
sleep(0.8)
print('PO!!!')
pygame.event.wait(2)

print('{}-'.format('-=' * 20))
print('Computador jogou {} \nJogador jogou {}'.format(opcoes[computador], opcoes[jogador]))
print('{}- \n'.format('-=' * 20))

if computador == jogador:
    print('{}EMPATE{}'.format('\033[1;34m', '\033[m'))
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print('{}COMPUTADOR VENCE{}'.format('\033[1;31m', '\033[m'))
else:
    print('{}JOGADOR VENCE{}'.format('\033[1;32m', '\033[m'))
