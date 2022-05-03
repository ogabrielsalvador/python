
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

soma = 0
men_idade = 0
men_nome = 0
woman = 0

for c in range(1, 5):
    print('{} {}ª PESSOA {}'.format('-' * 5, c, '-' * 5))
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma += idade
    if sexo != 'M' and sexo != 'F':
        print('{}Sexo digitado INVÁLIDO. Por favor digite novamente para prosseguir{}'.format('\033[1;31m', '\033[m'))
        exit()
    if sexo == 'M' and idade > men_idade:
        men_idade = idade
        men_nome = nome
    if sexo == 'F' and idade < 20:
        woman += 1

# media da idade
media = soma / 4
print('A média de idade do grupo é de {:.1f} anos'.format(media))

# nome do homem mais velho
if men_idade == 0:
    print('Não há homens nesse grupo')
else:
    print('O homem mais velho desse grupo tem {} anos e se chama {}'.format(men_idade, men_nome))

# qtde de mulheres com menos de 20 anos
if woman == 0:
    print('Não há mulheres com idade inferior a 20 anos nesse grupo')
elif woman == 1:
    print('Há apenas {} mulher com idade inferior a 20 anos nesse grupo'.format(woman))
else:
    print('Ao todos são {} mulheres com menos de 20 anos'.format(woman))
