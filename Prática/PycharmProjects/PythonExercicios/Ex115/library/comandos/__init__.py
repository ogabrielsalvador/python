from Ex115.library import interface


def leiaInt(text):
    while True:
        try:
            number = int(input(text))
            break
        except ValueError:
            print('\033[1;31mERRO! Por favor, digite um número inteiro válido...\033[m')
    return number


def fazerDict(text, quantity=0):
    if quantity == 0:
        quantity = leiaInt('Digite o tamanho do dict: ')
    dicionary = {}
    for c in range(quantity):
        descrition = str(input(text))
        dicionary[c + 1] = descrition
    return dicionary


def arquivoExiste(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivoCriar(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        print('ERRO! Não foi possível criar o arquivo.')
        print(TypeError)
    else:
        print(f'O arquivo {file} foi criado com sucesso.')


def arquivoLer(file, tam=42):
    try:
        a = open(file, 'rt')
    except:
        print('ERRO! Não foi possível ler o arquivo')
    else:
        interface.titulo('LISTA DE CADASTRO', tam)
        print(f'{"Nome":<{tam - 8}} Idade  ')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<{tam - 10}}{dados[1] + " anos ":>{10}}')
        a.close()


def arquivoCadastrar(file, name='< desconhecido >', age=0):
    try:
        a = open(file, 'at')
    except:
        print('ERRO! Não foi possível abrir o arquivo.')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('ERRO! Não foi possível cadastrar a pessoa na lista.')
        else:
            print(f'Novo registro de {name} finalizado com sucesso')
            a.close()
