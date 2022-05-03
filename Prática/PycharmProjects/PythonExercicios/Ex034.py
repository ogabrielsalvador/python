
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o seu salário para conferir qual será o seu aumento: R$ '))

if sal > 1250:
    novosal = sal * 1.1
else:
    novosal = sal * 1.15

print('O seu salário passará a ser de R$ {:.2f} \nTendo um aumento de R$ {:.2f}'.format(novosal, novosal - sal))
