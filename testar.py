

# @bool @complex @deque @dict @float @int @list @none @range @set @str @tuple

# d = {True: False, 7j: -7j, 'd': {'c': 'v'}, 1.0: 1.0, 7: 7, None: None, 's': 'S', ('t',): ('T',)}
# l = [True, 7j, {'c': 'v'}, 7.0, 7, ['l'], None, {'cj'}, 's', ('t',)]
# t = (True, 7j, {'c': 'v'}, 7.0, 7, ['l'], None, {'cj'}, 's', ('t',))
# cj = {True, 7j, 7.0, 7, None, 's', ('t',)}

# def scan(classe, dado):
#     try:
#         print(classe, dado.__abs__())
#     except AttributeError as error:
#         print('{}{}{}'.format('\033[1:31m', error, '\033[m'))
#
# scan('booleano', True)
# scan('complexo', 7j)
# scan('dicionário', {'c': 'v'})
# scan('flutuante', 7.0)
# scan('inteiro', 7)
# scan('lista', ['l'])
# scan('nenhum', None)
# scan('range', range(1, 4))
# scan('conjunto', {'cj'})
# scan('string', 's')
# scan('tupla', ('t',))

# i = int('1020', 7)
# print(i)
# print(format(i, 'b'))


# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete
