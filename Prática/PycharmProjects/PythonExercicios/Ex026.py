# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

import unidecode as unidecode

frase = str(input('Digite uma frase: ')).lower().strip()
letra = str(input('Qual a letra que você procura? ')).lower().strip()

# removendo os acentos
f = unidecode.unidecode(frase)
le = unidecode.unidecode(letra)

a = f.count(le)
a1 = f.find(le) + 1
a2 = f.rfind(le) + 1

print(f'A letra {le} aparece {a} vezes na frase')
print(f'A primeira letra {le} apareceu na posição {a1} \nA última letra {le} apareceu na posição {a2}')
