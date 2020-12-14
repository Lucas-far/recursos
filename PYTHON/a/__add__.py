

"""
Objetivo:
    executar subtração ou soma entre classes numéricas

Objetivo 2:
    adicionar dados à classes iteráveis: lista, string e tupla

Observação:
    1. pode ser usado em classe booleano, onde argumentos nomeados: bool & int (confuso)
"""

# @bool @complex @float @int @list @str @tuple

def scan(classe, dado, valor):
    try:
        print(classe, dado, dado.__add__(valor))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, 3j)
scan('dicionário', {}, {-7: -7})
scan('flutuante', 7.0, -7.0)
scan('inteiro', 7, -7)
scan('lista', [], [-7])
scan('nenhum', None, 0)
scan('range', range(1, 4), range(5, 6))
scan('conjunto', {7}, {3})
scan('string', 'pyt', 'hon')
scan('tupla', (), (0,))
