

"""
Objetivo:
    especificar mais de um tipo de classe que um parâmetro pode aceitar
"""

from random import choice
from typing import Union

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 16:30
    """

# Exemplo em parâmetros
def mais_menos(operador: str, valor: Union[int, float], valor2: Union[int, float]) -> None:
    if operador == '+':
        print(f'A soma de {valor} + {valor2} é igual a: {valor + valor2}')
    elif operador == '-':
        print(f'A subtração de {valor} - {valor2} é igual a: {valor - valor2}')
    else:
        print(f'\n========== Erro ==========\nOperador inválido: {operador!r}')

mais_menos('-', 7.7, 12.3)
mais_menos('+', 13, 7)

# Em caso de parâmetros inesperados, ou seja, fora do escopo de Union[]
"mais_menos('-', 90.5, 20j)"  # Expected type 'Union[int, float]', got 'complex' instead

# Exemplo em retorno (condições são mandatórias para definir em qual contexto cada tipo será usado)
def meses() -> Union[str, list, tuple]:
    l = choice('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split())
    if l == 'janeiro' or l == 'fevereiro' or l == 'março' or l == 'abril':
        return l
    elif l == 'maio' or l == 'junho' or l == 'julho' or l == 'agosto':
        return [l]   # list(l)
    else:
        return l,  # tuple(l)

print(meses())
