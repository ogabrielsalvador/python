
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
# mas com uma validação de dados para aceitar apenas valores que seja monetário.

from Ex112.utilidades import moeda, dado

preco = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 10, 20)
