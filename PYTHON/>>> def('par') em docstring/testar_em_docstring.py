

def contar_caracteres(texto):
    """
    >>> assert contar_caracteres('banana') 'contagem errada'
    a: 3
    b: 1
    n: 2
    """

    "Poderia ser..."
    # >>> contar_caracteres('banana')

    from collections import Counter

    counter = sorted("".join(texto.split()))
    counter = dict(Counter(counter))

    for key, value in counter.items():
        print(key + ':', value)

if __name__ == '__main__':
    contar_caracteres('banana')
