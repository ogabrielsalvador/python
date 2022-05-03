
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while

print('{}\n{} 10 PRIMEIROS TERMOS DE UMA PA{}\n{}'.format('=' * 31, '\033[1;36m', '\033[m', '=' * 31))
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

pa = a1
c = 1

while c <= 10:
    print(pa, end=' → ')
    pa = pa + r
    c += 1
print('FIM')
