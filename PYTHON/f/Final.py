

"""
Objetivo:
    informar que uma variável constante não deve receber alteração

Observação:
    1. apesar de ferramentas como o mypy avisarem que não deve-se redeclarar uma var constante, isso não é impedido
"""

from typing import Final

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 18:50
    """

"terminal"  # não detecta o erro, nem impede
"mypy"      # detecta o erro, não impede

NOME: Final = 'desconhecido'
NOME = '...'  # 'NOME' is 'Final' and could not be reassigned
print(NOME)

def reportar() -> None:
    """
    Final.py:16: error: Cannot assign to final name "NOME
    Found 1 error in 1 file (checked 1 source file)
    """
print(reportar.__doc__)
