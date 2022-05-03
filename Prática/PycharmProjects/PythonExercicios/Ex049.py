
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

n = int(input('Digite um número para ver a sua tabuada: '))
print('{}\n{}-  TABUADA DO {}  {}-\n{}'.format('\033[1;35m', '-=' * 4, n, '-=' * 4, '\033[m'))

for c in range(1, 11):
    p = n * c
    print('{} x {:2} = {}'.format(n, c, p))
