

"""
Objetivo:
    testar o tempo de execução de códigos em string, seja em literal ou variáveis
"""

from timeit import timeit

print([1], v := timeit('list(range(1, 100))', globals=globals()))
print([2], timeit('list(range(1, 100))'))
print([3], timeit("[each_letter for each_letter in 'string'*50]"))
print([4], timeit("[each_letter for each_letter in 'string'*50]", globals=globals()))
