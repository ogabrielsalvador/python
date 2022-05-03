n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# uso do ':.3f' dentro do conchetes para determinar o número de casas decimais

print('O valor da soma é {}, o do produto é {} e o da divisão é {:.2f}'.format(soma, m, d))
print('O valor da divisão inteira é {} e o da potência é {}'.format(di, e))

# uso do 'end' para não ter a quebra de linha

print('O valor da soma é {}, o do produto é {} e o da divisão é {:.2f}'.format(soma, m, d), end='. ')
print('O valor da divisão inteira é {} e o da potência é {}'.format(di, e))

# uso do '\n' para ter a quebra de linha

print('O valor da soma é {}, \n o do produto é {} \n e o da divisão é {:.2f}'.format(soma, m, d))
print('O valor da divisão inteira é {} e o da potência é {}'.format(di, e))
