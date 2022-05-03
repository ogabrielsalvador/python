
titulo = 'CAIXA ELETRÔNICO'
print('{}\n{}{}{}\n{}'.format('=' * 30, '\033[1;31m', titulo.center(30), '\033[m', '=' * 30))

saque = int(input('Qual o valor que você quer sacar? R$ '))

resto_saque = saque
v_cedula = 50
n_cedula = 0

while True:
    if resto_saque >= v_cedula:
        resto_saque -= v_cedula
        n_cedula += 1
    else:
        if n_cedula > 0:
            print(f'Total de {n_cedula} cédulas de R$ {v_cedula}')
        if v_cedula == 50:
            v_cedula = 20
        elif v_cedula == 20:
            v_cedula = 10
        elif v_cedula == 10:
            v_cedula = 1
        n_cedula = 0
        if resto_saque == 0:
            break

