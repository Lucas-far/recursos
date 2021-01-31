

"""

"""

from random import choice

def escolher_video():
    """"""
    # 'neuralnine', 'online tutorials' 'python pro django'
    escolha = choice(['python pro pytools', 'udemy bdd', 'udemy js', 'udemy python'])
    return escolha

if __name__ == '__main__':
    print(escolher_video())
