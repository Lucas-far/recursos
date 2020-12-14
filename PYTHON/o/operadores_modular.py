

"""
Objetivo:
    verificar se um número é par ou ímpar

Objetivo 2:
    analizar iteráveis para filtrar dados
"""

# Verificando por ou ímpar
v = 0
if v % 2 == 0:
    print(f'O número {v} é par')
else:
    print(f'O número {v} é ímpar')

# Exemplos de operações modular
print([1], [x for x in [*range(1, 28)] if x % 7 == 0])  # [7, 14, 21]
print([2], [x for x in [*range(1, 28)] if not x % 7])   # igual [1]
print([3], [x for x in [*range(1, 28)] if x % 2])       # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
print([4], [x for x in [*range(1, 28)] if not x % 2])   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
print([5], [x for x in [*range(1, 28)] if x % 2 == 1])  # igual [3]
print([6], [x for x in [*range(1, 28)] if x % 2 == 0])  # igual [4]
