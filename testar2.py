

class Motor:

    def __init__(self):
        self.__velocidade = 0
        self.__aero = True

    def acelerar(self):
        self.__velocidade += 1

    def frear(self):
        self.__velocidade -= 2
        self.__velocidade = max(0, self.__velocidade)
        # if self.__velocidade < 0:
        #     self.__velocidade = 0

    def calcular_velocidade(self):
        return self.__velocidade

motor = Motor()
print(motor.__dict__)
