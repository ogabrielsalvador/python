
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# -> IMC abaixo de 18,5: Abaixo do Peso -> Entre 18,5 e 25: Peso Ideal -> 25 até 30: Sobrepeso
# -> 30 até 40: Obesidade -> Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f} \nVocê está ABAIXO DO PESO'.format(imc))
elif imc < 25:
    print('O IMC dessa pessoa é de {:.1f} \nVocê está no PESO IDEAL'.format(imc))
elif imc < 30:
    print('O IMC dessa pessoa é de {:.1f} \nVocê está em SOBREPESO'.format(imc))
elif imc < 40:
    print('O IMC dessa pessoa é de {:.1f} \nVocê está em OBESIDADE'.format(imc))
else:
    print('O IMC dessa pessoa é de {:.1f} \nVocê está em OBESIDADE MÓRBIDA'.format(imc))
