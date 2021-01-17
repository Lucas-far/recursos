

"""
Módulo: testar_em_docstring.py

Objetivo:
         inserir testes em métodos através de suas docstrings

Palavra chave: testar docstring
"""

"OBS"  # assert poderia ou não estar no contexto
"OBS"  # essa forma de teste é básica, não recomendado seu uso
def contar_caracteres(texto):
    """
    >>> assert contar_caracteres('banana') 'contagem errada'
    a: 3
    b: 1
    n: 2
    """

    from collections import Counter

    counter = sorted("".join(texto.split()))
    counter = dict(Counter(counter))

    for key, value in counter.items():
        print(key + ':', value)

if __name__ == '__main__':
    contar_caracteres('banana')
