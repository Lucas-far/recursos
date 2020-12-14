

"""
Objetivo:
    mostrar duas formas de deletar chaves de uma classe dicionário
"""
# todo Tutorial 8

print([1], d := {'x': 1, 'y': 2, 'z': 3})

# Método 1
d.pop('z'), print([2], d)

# Método 2
del d['x']
print([3], d)
