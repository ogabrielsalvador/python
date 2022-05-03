# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas
# - Quantas letras no total (sem considerar espeaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome? ')).strip()

# deixando o nome em letras maiúsculas e minúsculas

nomeG = nome.upper()
nomeP = nome.lower()

# contando o total de letras

nomeespaco = nome.count(' ')
nomeletra = len(nome) - nomeespaco

# separando as palavras e usando a primeira

lista = nome.split()
nome1 = lista[0]
nomeletra1 = len(nome1)

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}\nSeu nome em minúsculas é {}'.format(nomeG, nomeP))
print('Seu nome tem ao todo {} letras'.format(nomeletra))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1, nomeletra1))
