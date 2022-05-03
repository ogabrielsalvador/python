
# Vamos criar um menu em Python, usando modularização.

from Ex115.library import interface

larg = 45       # largura da tabela.
dict_opcoes = {1: 'Lista de Cadastro', 2: 'Cadastrar nova Pessoa', 3: 'Sair do Sistema'}     # São as opções que aparecem no menu.

while True:
    interface.titulo('MENU PRINCIPAL', larg)
    interface.menu(dict_opcoes)
    opcao = interface.opcao('Digite a sua opção: ', len(dict_opcoes), larg)
    if opcao == 3:
        interface.encerrar(larg)
        break
