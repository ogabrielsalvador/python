
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerrará quando ele disser que quer mostrar 0 termos

print('{}\n{} 10 PRIMEIROS TERMOS DE UMA PA{}\n{}'.format('=' * 31, '\033[1;36m', '\033[m', '=' * 31))
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

pa = a1
final = a1 + (r * 10)
c = 0
opcao = 1

while pa != final:
    print(pa, end=' → ')
    pa += r
    c += 1
print('PAUSA')

while opcao != 0:
    opcao = int(input('Quantos termos você quer mostrar a mais? '))
    final = pa + (r * opcao)
    while pa != final:
        print(pa, end=' → ')
        pa += r
        c += 1
        if pa == final:
            print('PAUSA')
print(f'Progressão finalizada com {c} termos mostrados')
