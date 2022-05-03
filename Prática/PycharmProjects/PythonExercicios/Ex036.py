
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretender quitar o empréstimo? '))

prestacao = casa / (anos * 12)

if prestacao <= (salario * 0.3):
    print('O seu empréstimo bancário foi CONCEDIDO! PARABÉNS!')
else:
    print('Seu empréstimo foi NEGADO.')
