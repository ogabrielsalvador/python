
# Esse arquivo é o módulo 'moeda.py' do Ex 107


def aumentar(price, percentage):
    return price * (1 + (percentage / 100))


def diminuir(price, percentage):
    return price * (1 - (percentage / 100))


def dobro(price):
    return price * 2


def metade(price):
    return price / 2
