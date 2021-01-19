

"""
Último acesso: PYTHON/d/DictWriter.py
"""

from random import choice

def escolher_video():
    """"""
    escolha = choice(['neuralnine', 'online tutorials', 'python pro django', 'python pro pytools', 'udemy bdd',
                     'udemy js', 'udemy python'])
    return escolha

if __name__ == '__main__':
    print(escolher_video())
