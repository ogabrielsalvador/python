
# Elabore um programa que calcule o valor a pagar por um produto, considere o seu preço normal e condição de pagamento:
# -> à vista dinheiro/cheque: 10% de desconto -> à vista no cartão: 5% de desconto
# -> em até 2x no cartão: preço formal -> 3x ou mais no cartão: 20% de juros

print(' ')
print('{}{} GAEL STORE {}{}'.format('=' * 10, '\033[1;31;107m', '\033[m', '=' * 10))
print(' ')

preco_atual = float(input('Preço das compras: R$ '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    preco_final = preco_atual * 0.9
    print('Sua compra será à vista COM 10% DE DESCONTO \nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'
          .format(preco_atual, preco_final))
elif opcao == 2:
    preco_final = preco_atual * 0.95
    print('Sua compra será à vista COM 5% DE DESCONTO \nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'
          .format(preco_atual, preco_final))
elif opcao == 3:
    preco_final = preco_atual
    parcela = preco_final / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS \nSua compra vai custar R$ {:.2f} no final.'
          .format(parcela, preco_final))
elif opcao == 4:
    n = int(input('Quantas parcelas? '))
    preco_final = preco_atual * 1.2
    parcela = preco_final / n
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS \nSua compra de {:.2f} vai custar R$ {:.2f} no final.'
          .format(n, parcela, preco_atual, preco_final))
else:
    print('A opção digitada é INVÁLIDA, por favor digite novamente!')
