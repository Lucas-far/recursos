

"""
Objetivo:
    converter uma classe inteira para sua versão octal, mas não é uma classe

Observação:
    1. ao testar o tipo de um dado octal, o retorno é uma string (confuso)
"""

# @bool @int

def scan(classe, dado):
    try:
        print(classe, oct(dado))
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

print([1], oct(10))
print([2], v := oct(99))
