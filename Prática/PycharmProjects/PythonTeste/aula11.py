
# Cores no Terminal

# 'nome' com estilo em negrito, letra preta e fundo branco:

nome = str(input('Qual o seu nome? ')).title()

# forma 01 de fazer
print(f'Seja bem vindo, \033[1;30;107m{nome}\033[m!')
print(' ')     # esse espaço é só pra ficar melhor de vizualizar os resultados

# forma 02
print('Seja bem vindo, {}{}{}!'.format('\033[1;30;107m', nome, '\033[m'))
print(' ')

# forma 03 (recomendado para códigos maiores onde as cores serão utilizadas mais de uma vez)
estilos = {'limpa': '\033[m',
           'pretoebranco': '\033[1;30;107m',
           'azulecinza': '\033[1;34;47m'}
print('Seja bem vindo, {}{}{}!'.format(estilos['pretoebranco'], nome, estilos['limpa']))
