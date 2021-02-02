

"""

"""

from random import shuffle

def escolher_video():
    """"""
    # 'neuralnine', 'online tutorials' 'python pro django'
    escolha = ['python', 'python pro pytools', 'udemy bdd', 'udemy js', 'udemy python']
    shuffle(escolha)
    return escolha

if __name__ == '__main__':
    print(var := escolher_video())
    # ['udemy js', 'udemy python', 'udemy bdd', 'python', 'python pro pytools']
