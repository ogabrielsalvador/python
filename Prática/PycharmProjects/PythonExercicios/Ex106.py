
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep


cores = ('\033[m',          # 0 - sem cor
         '\033[7;97m',      # 1 - branco
         '\033[1;30;41m',   # 2 - vermelho
         '\033[1;30;42m',   # 3 - verde
         '\033[1;30;43m',   # 4 - amarelo
         '\033[1;30;44m',   # 5 - azul
         '\033[1;30:45m',   # 6 - sem cor
         '\033[1;30;46m',   # 7 - azul
         '\033[1;30;47m',   # 8 - cinza
         '\033[1;97m',      # 9 - preto
         )


def titulo(title, color=0):
    print(f'{cores[color]}{"=" * (len(title) + 4):^{len(title) + 12}}{cores[0]}\n'
          f'{cores[color]}{title:^{len(title) + 12}}{cores[0]}\n'
          f'{cores[color]}{"=" * (len(title) + 4):^{len(title) + 12}}{cores[0]}')


def ajuda(comand, color=0):
    print(cores[color])
    print(help(comand))
    print(cores[0])


while True:
    titulo('SISTEMA DE AJUDA DO GAELzinho', 7)
    txt = str(input(f'{cores[4]}Função ou Biblioteca -> {cores[0]}  ')).strip()
    if txt.upper() == 'FIM':
        break
    titulo(f'Acessando o manual do {txt}:', 1)
    sleep(0.4)
    ajuda(txt, 8)
    sleep(1.5)

print(f'{cores[3]}  ENCERRANDO PROGRAMA...  {cores[0]}')
sleep(1)
titulo('PROGRAMA ENCERRADO', 2)
