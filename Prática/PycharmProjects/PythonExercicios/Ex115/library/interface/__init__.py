
def linha(tam=42):
    print('-' * tam)


def titulo(txt, tam=42):
    linha(tam)
    print(f'\033[1m{txt:^{tam}}\033[m')
    linha(tam)


def opcao(text, quantity, tam=42):
    from Ex115.library.comandos import leiaInt
    linha(tam)
    while True:
        try:
            option = leiaInt(text)
        except KeyboardInterrupt:
            print('\n\033[1;33mO usuário preferiu não digitar uma opção...\033[m')
            option = 3
        if 0 < option <= quantity:
            break
        print(f'\033[1;31mERRO! Por favor, digite uma opção válida...\033[m')
    linha(tam)
    print(f'\033[1;32m{"OPÇÃO " + str(option):^{tam}}\033[m')
    return option


def menu(dicionary):
    for k, v in dicionary.items():
        print(f'\033[1;33m {k} -\033[34m {v}\033[m')


def encerrar(tam=42):
    from time import sleep
    linha(tam)
    print(f'{"Encerrando programa... Volte sempre!":^{tam}}')
    linha(tam)
    for c in range(3):
        sleep(0.4)
        print(f'{".":^{tam}}')
    sleep(0.5)
    print(f'\033[1;31m{"PROGRAMA ENCERRADO COM SUCESSO!":^{tam}}\033[m')
