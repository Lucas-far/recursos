

class Cachorro:  # criação da classe
    # atributos de classe
    frase = 'Eu não sou seu amigo, kkk'
    frase2 = 'Eu estou cansado, vou dormir :)!'
    frase3 = 'Onde está o meu lanche? U.U'
    frase4 = 'Eu acho que vou banhar T-T'
    frases = [frase, frase2, frase3, frase4]

    @classmethod
    def dizer_frase(cls, index):  # atributo de classe / imprimir
        print(cls.frases[index])

    @classmethod
    def mudar_frase(cls, index, nova_frase):  # atributo de classe / alterar
        cls.frases[index] = nova_frase

    @staticmethod
    def mensagem():  # método estático (não está ligado aos atributos de classe ou instância)
        print(f'BEM-VINDO \ ^^ /')

    @property
    def nome(self):  # atributo de instância / retornar / antes de __init__ / mandatorio: return e .__
        return self.__nome

    @nome.setter
    def nome(self, novo_valor):  # atributo de instância / alterar / anterior / mandatorio: .__
        self.__nome = novo_valor

    def __init__(self, nome: str = 'vazio', *cores):  # método inicializador / atributos de instância
        self.__nome = nome                            # declaração dos atributos (instância e classe)
        self.__cores = list(cores)
        Cachorro.altura = 'atributo de classe'        # definindo um atrib. classe (não recomendado fazer aqui)
        self._exibir_cores()

    def _exibir_cores(self):
        print([1], self.__cores)

if __name__ == '__main__':
    rufus = Cachorro('Rufus', 'preto', 'branco')
    print([2], rufus.__dict__)
    rufus.dizer_frase(0)                                  # atributo de classe (chamada)
    rufus.mudar_frase(0, 'Eu quero brincar, humano! :P')  # atributo de classe (alteração)
    rufus.dizer_frase(0)
    rufus.idade = 10                                      # criação de atributo dinâmico
    print([3], rufus.idade)
    rufus.mensagem()                                      # def mensagem (uso)
    print([4], rufus.nome)                                # def nome (uso) (@property)
    rufus.nome = 'Leonidas'                               # def nome (uso) (@nome.setter)
    print([5], rufus.nome)
    print([6], rufus.__init__.__annotations__)            # mostrar tipos em def __init__
    print([7], rufus.__dict__)
    del rufus.idade                                       # deletar atributo dinâmico, ou classe, ou de instância)
    print([8], rufus.__dict__)
