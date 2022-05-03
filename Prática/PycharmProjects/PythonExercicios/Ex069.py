
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = homem = mulher = 0
while True:
    print('{}\n   {}CADASTRE UMA PESSOA{}\n{}'.format('-' * 25, '\033[1;33m', '\033[m', '-' * 25))
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo in 'MF':
            break
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-' * 25)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('=' * 25)
print(f'Total de pessoas com mais de 18 anos: {maior}\nAo todo temos {homem} homens cadastrados\n'
      f'E temos {mulher} mulheres com menos de 20 anos')
print('=' * 25)
