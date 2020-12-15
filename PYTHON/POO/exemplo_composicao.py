

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


#
#     def __init__(self, sentido, velocidade):
#         super().__init__(sentido)
#         super().__init__(velocidade)
#


    # def frear(self):
    #     self.motor.frear()
    #
    # def calcular_velocidade(self):
    #     return self.motor.velocidade
    #
    # def calcular_sentido(self):
    #     return self.sentido.sentido
    #
    # def sentido_girar_direita(self):
    #     self.sentido.sentido_girar_direita()
    #
    # def sentido_girar_esquerda(self):
    #     self.sentido.sentido_girar_esquerda()

# class Carro:  # class Carro(Sentido, Motor)
#
#     # def __init__(self, sentido, velocidade):
#     #     super().__init__(sentido)
#     #     super().__init__(velocidade)
#     def __init__(self, sentido, motor):
#         self.sentido = sentido
#         self.motor = motor
#
#     def acelerar(self):
#         self.motor.acelerar()
#
#     def frear(self):
#         self.motor.frear()
#
#     def calcular_velocidade(self):
#         return self.motor.velocidade
#
#     def calcular_sentido(self):
#         return self.sentido.sentido
#
#     def sentido_girar_direita(self):
#         self.sentido.sentido_girar_direita()
#
#     def sentido_girar_esquerda(self):
#         self.sentido.sentido_girar_esquerda()

if __name__ == '__main__':
    pass
