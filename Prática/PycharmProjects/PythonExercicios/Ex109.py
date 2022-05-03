
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from Ex109 import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.')
print(f'Com um aumento de 10% o preço será de {moeda.aumentar(preco, 10, True)}.')
print(f'Com um desconto de 20% o preço será de {moeda.diminuir(preco, 20, True)}.')
