# Vamos finalizar o projeto de acesso a arquivos em Python.

from Ex115.library.interface import *
from Ex115.library.comandos import *

larg = 45       # largura da tabela.
dict_opcoes = {1: 'Lista de Cadastro', 2: 'Cadastrar nova Pessoa', 3: 'Sair do Sistema'}     # São as opções que aparecem no menu.

arquivo = 'Ex115_arquivo'
if not arquivoExiste(arquivo):
    arquivoCriar(arquivo)

while True:
    titulo('MENU PRINCIPAL', larg)
    menu(dict_opcoes)
    resposta = opcao('Digite a sua opção: ', len(dict_opcoes), larg)
    if resposta == 1:
        arquivoLer(arquivo, larg)
    elif resposta == 2:
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        arquivoCadastrar(arquivo, nome, idade)
    if resposta == 3:
        encerrar(larg)
        break
