
# Esse arquivo é o módulo 'moeda.py' do Ex108


def aumentar(price=0, percentage=0):
    return price * (1 + (percentage / 100))


def diminuir(price=0, percentage=0):
    return price * (1 - (percentage / 100))


def dobro(price=0):
    return price * 2


def metade(price=0):
    return price / 2


def moeda(price=0, unity='R$'):
    return f'{unity} {price:.2f}'.replace('.', ',')
