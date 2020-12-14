

"""
Objetivo:
    não sei o objetivo, precisa de mais pesquisa
"""

l = [9.4, 2.7, 5.6, 3.3, 2.9]
print([1], tuple(map(lambda v: f"{v + 0.1:.1f}", l)))
print([2], tuple(f"{x + 0.1:.1f}" for x in l))
