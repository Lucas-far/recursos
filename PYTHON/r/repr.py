

from datetime import datetime

def infos():
    """
    Objetivo:
         retornar a representação da construção de uma data, como no método datetime()

    Objetivo 2:
        /home/lucas/PycharmProjects/recursos/PYTHON/r/!r.py
    """

def scan(classe, dado):
    try:
        print(classe, repr(dado))
    except AttributeError as error:
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

print([1], dt := datetime.now())  # a data possui um formato
print([2], repr(dt))              # repr() cria uma representação dessa data
