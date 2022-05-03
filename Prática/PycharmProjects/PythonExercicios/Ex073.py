
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

# item A):
print('Os cinco primeiros colocados são:', end=' ')
for c in range(0, 5):
    if c == 4:
        print(f'{c + 1}º {times[c]}.')
    else:
        print(f'{c + 1}º {times[c]}', end=', ')

# item B):
print('Os quatro últimos colocados são:', end=' ')
for c in range(16, 20):
    if c == 19:
        print(f'{c + 1}º {times[c]}.')
    else:
        print(f'{c + 1}º {times[c]}', end=', ')

# item C):
ordem_alf = sorted(times)
print('Os times em ordem alfabética:', end=' ')
for c in range(0, 20):
    if c == 19:
        print(f'{ordem_alf[c]}.')
    else:
        print(f'{ordem_alf[c]}', end=', ')

# item D):
print(f'O time da Chapecoense está na {times.index("Chapecoense") + 1}ª colocação.')
