

"""
Objetivo:
    usado em classes iteráveis para percorrer seus dados de forma específica, escolhendo saltá-los ou não

Observação:
    1. não recomenda-se o uso em classe conjunto, pois o posicionamento dos dados é aleatório
"""

# @dict @list @range @set @str @tuple

def scan(classe, dado):
    try:
        var = iter(dado)
        print(classe, next(var))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {'c': 'v'})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', ['l'])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {'cj'})
scan('string', 's')
scan('tupla', ('t',))

s = iter('carpe diem')
next(s), print([0], next(s), next(s), next(s)), next(s), next(s), print([1], next(s), next(s))
