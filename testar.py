

"""
>>> motor = Motor()
>>> motor.calcular_velocidade()
0

>>> motor.acelerar()
>>> motor.calcular_velocidade()
1

>>> motor.acelerar()
>>> motor.calcular_velocidade()
2

>>> motor.frear()
>>> motor.calcular_velocidade()
0





>>> direcao = Direcao()
>>> direcao.valor()
'Norte'

>>> direcao.girar_a_direita()
>>> direcao.valor()
'Leste'

>>> direcao.girar_a_direita()
>>> direcao.valor()
'Sul'

>>> direcao.girar_a_direita()
>>> direcao.valor()
'Oeste'

>>> direcao.girar_a_direita()
>>> direcao.valor()
'Norte'


>>> direcao.girar_a_esquerda()
>>> direcao.valor()
'Oeste'

>>> direcao.girar_a_esquerda()
>>> direcao.valor()
'Sul'

>>> direcao.girar_a_esquerda()
>>> direcao.valor()
'Leste'

>>> direcao.girar_a_esquerda()
>>> direcao.valor()
'Norte'





>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0

>>> carro.acelerar()
>>> carro.calcular_velocidade()
1

>>> carro.acelerar()
>>> carro.calcular_velocidade()
2

>>> carro.frear()
>>> carro.calcular_velocidade()
0

>>> carro.calcular_direcao()
'Norte'

>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'

>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'

>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""

# todo Dados complementares para esse módulo:
#     home/lucas/PycharmProjects/recursos/PYTHON/POO/doctest_infos.py

class Carro:

    def __init__(self, direcao, motor):
        self.__motor = motor
        self.__direcao = direcao

    def acelerar(self):
        self.__motor.acelerar()

    def frear(self):
        self.__motor.frear()

    def calcular_velocidade(self):
        return self.__motor.calcular_velocidade()

    def calcular_direcao(self):
        return self.__direcao.valor()

    def girar_a_direita(self):
        self.__direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.__direcao.girar_a_esquerda()

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:

    girar_direita_logica = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    girar_esquerda_logica = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.__valor = NORTE

    def valor(self):
        return self.__valor

    def girar_a_direita(self):
        self.__valor = self.girar_direita_logica[self.__valor]
        # if self.__sentido == 'Norte':
        #     self.__sentido = 'Leste'
        # elif self.__sentido == 'Leste':
        #     self.__sentido = 'Sul'
        # elif self.__sentido == 'Sul':
        #     self.__sentido = 'Oeste'
        # else:
        #     self.__sentido = 'Norte'

    def girar_a_esquerda(self):
        self.__valor = self.girar_esquerda_logica[self.__valor]
        # if self.__sentido == 'Norte':
        #     self.__sentido = 'Oeste'
        # elif self.__sentido == 'Oeste':
        #     self.__sentido = 'Sul'
        # elif self.__sentido == 'Sul':
        #     self.__sentido = 'Leste'
        # else:
        #     self.__sentido = 'Norte'

class Motor:

    def __init__(self):
        self.__velocidade = 0

    def acelerar(self):
        self.__velocidade += 1

    def frear(self):
        self.__velocidade -= 2
        self.__velocidade = max(0, self.__velocidade)
        # if self.__velocidade < 0:
        #     self.__velocidade = 0

    def calcular_velocidade(self):
        return self.__velocidade

if __name__ == '__main__':
    pass

def tutorial():
    """
    1. Uma classe [ Motor ] é criada
    2. Nota-se que nao há atribs. inst. dentro do método __init__
    3. Porém, se no escopo de declaração há [ self.var ], esta será interpretada como atrib. inst. (não obrigatória)
    4. Os três métodos nela existentes
    """

# @bool @complex @deque @dict @float @int @list @none @range @set @str @tuple

# d = {True: False, 7j: -7j, 'd': {'c': 'v'}, 1.0: 1.0, 7: 7, None: None, 's': 'S', ('t',): ('T',)}
# l = [True, 7j, {'c': 'v'}, 7.0, 7, ['l'], None, {'cj'}, 's', ('t',)]
# t = (True, 7j, {'c': 'v'}, 7.0, 7, ['l'], None, {'cj'}, 's', ('t',))
# cj = {True, 7j, 7.0, 7, None, 's', ('t',)}

# def scan(classe, dado):
#     try:
#         print(classe, dado.__abs__())
#     except AttributeError as error:
#         print('{}{}{}'.format('\033[1:31m', error, '\033[m'))
#
# scan('booleano', True)
# scan('complexo', 7j)
# scan('dicionário', {'c': 'v'})
# scan('flutuante', 7.0)
# scan('inteiro', 7)
# scan('lista', ['l'])
# scan('nenhum', None)
# scan('range', range(1, 4))
# scan('conjunto', {'cj'})
# scan('string', 's')
# scan('tupla', ('t',))
