
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(text='Digite um número inteiro: '):
    while True:
        try:
            number = int(input(text))
            return number
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Não foi digitado um número inteiro.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            return 0


def leiaFloat(text='Digite um número real: '):
    while True:
        try:
            number = float(input(text))
            return number
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Não foi digitado um número real.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            return 0


nInt = leiaInt()
nFloat = leiaFloat()
print(f'O número inteiro digitado foi {nInt}.\nO número real digitado foi {nFloat}.')
