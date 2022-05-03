
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print(f'{"~" * (len(msg) + 4)}')
    print(f'  {msg}  ')
    print(f'{"~" * (len(msg) + 4)}')


# pode fazer assim...
texto = str(input('Digite o texto que você deseja: '))
escreva(texto)

# ou assim... (nesse caso sem declarar uma variável)
escreva(str(input('Digite o texto que você deseja: ')))
