
# Crie um pacote chamado utilidadesCeV que tenha dois Ex107 internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from Ex111.utilidades import moeda

preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 10, 20)
