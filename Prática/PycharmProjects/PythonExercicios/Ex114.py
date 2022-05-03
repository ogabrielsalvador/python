
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import webbrowser
import urllib.request

url = 'http://www.pudim.com.br'

try:
    site = urllib.request.urlopen(url)
except urllib.error.URLError:       # descrição do tipo de erro que ocorre
    print('Página não acessada.')
else:
    print('Página acessada com sucesso.')
    print(site.read())

# a biblioteca webbrowser pega a url fornecida e abre ela no navegador do computador.
webbrowser.open(url, new=0, autoraise=True)
webbrowser.open_new(url)        # [outra maneira de abrir uma página]
