
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

n = float(input('Digite a velocidade do carro: '))

if n <= 80:
    print('Você está dentro do limite de velocidade.')
else:
    multa = (n - 80) * 7
    print('Você foi multado! O valor da sua multa é de R$ {:.2f}'.format(multa))
