
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('Quantos km foram percorridos? '))
dia = int(input('Por quantos dias o carro foi alugado? '))

custokm = km * 0.15
custodia = dia * 60
custototal = custokm + custodia

print('O preço a pagar é de R$ {:.2f} \n Sendo R$ {:.2f} refentes aos km percorridos \n E R$ {:.2f} pelos {} dias '
      'alugados'.format(custototal, custokm, custodia, dia))
