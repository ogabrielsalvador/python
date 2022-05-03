
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from Ex108 import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}.')
print(f'Com um aumento de 10% o preço será de {moeda.moeda(moeda.aumentar(preco, 10))}.')
print(f'Com um desconto de 20% o preço será de {moeda.moeda(moeda.diminuir(preco, 20))}.')
