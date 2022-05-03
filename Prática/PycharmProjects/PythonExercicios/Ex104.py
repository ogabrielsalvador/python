
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leia_int(msg=''):
    """
    → Recebe a entrada da str que vai aparecer ao usuário, solicita o input de uma str,
    valida se essa str pode ser um int e caso sim: retorna um int.
    :param msg: é a str que vai aparecer ao usuário [opcional].
    :return: retorna um número inteiro (int).
    """
    while True:
        number = input(msg)
        if number.strip().replace('-', '').isdigit():
            break
        print('\033[1;31mERRO! Digite um número inteiro...\033[m')
    return int(number)


n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}.')
