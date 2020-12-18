

# todo CURSO: Python Birds / AULA: Github e Setup

def fork():
    """
    1. Criar uma conta no GitHub (nesse caso, eu já possuo)
    2. Ir ao repositório: https://github.com/pythonprobr/pythonbirds
    3. Clicar em: [ fork ]
    5. Clicar em: [ code ] = [ https ]
    6. Copiar o link: [ https://github.com/Lucas-far/pythonbirds.git ] (no contexto da minha conta)
    """

def usar_projeto():
    """
    1. Reabrir o Pycharm
    2. Na tela de início, clicar em: [ get from version control ]
    3. Selecionar: [ Git ]
    4. Colar o https mencionado em 6
    5. Clicar em: [ clone ]
    6. O projeto deve abrir no seu Pycharm

       LÓGICA:
              Como o projeto já existe, eu estou supondo que o interpretador não seja local

    7. No Pycharm: [ File / Settings... / pesquisar: interpreter / clicar na seta para baixo ]
    8. Pela lógica acima, então deve-se escolher o interpretador: [ /usr/bin/python3.8 ]
    """

# Acessar jogo dentro e fora do Pycharm
def testar_jogo():
    """
    DENTRO:
           1. botão direito em: [ placa_grafica_tkinter.py ] = [ run ]

    FORA:
         1. navegar pelo diretório do projeto, no meu contexto, seria: [ /home/lucas/PycharmProjects/pythonbirds ]
         2. para então fazer: [ python3 placa_grafica_tkinter.py ]
    """

# todo CURSO: Python Birds / AULA: Commit e Push

def criar_commit_local():
    """
    Criar commits
    ------------------------------------------------
    raiz / botão direito / git / commit directory...
    ------------------------------------------------

    Objetivo:
        1. criar um commit para quando é feita uma mudança de projeto

    Observação:
        1. há uma região de texto destinada a descrição das mudanças feitas
        2. ao término, clicar no botão: [ commit ]
        3. os commits são registrados, parar posteriormente serem salvos de forma permanente
    """

def efetuar_push():
    """
    Efetuar push nos commits
    ---------------------------------
    raiz / botão direito / git / push
    ---------------------------------

    Objetivo:
        1. efetuar commits registrados, para quando um projeto seja usado (modo produção)
    """

# todo CURSO: Python Birds / AULA: Atributo Complexo

def classe_4():
    """
    class Pessoa:
        def __init__(self, nome: str = 'indefinido', idade: int = 18, *filhos):  # iterável (certo = *) (errado = [])
            self.nome = nome
            self.idade = idade
            self.filhos = list(filhos)

    if __name__ == '__main__':
        # obj
        alfa = Pessoa('Kano', 42, 'Marcos', 'Ângela')

        # obj2
        beta = Pessoa('Ermac', 39, alfa)  # obj dentro do obj2

        # RESOLUÇÃO 1
        for filho in beta.filhos:  # for var in obj.alfa-atrib3
            print(filho.nome)      # print(var.alfa.atrib1)

        # RESOLUÇÃO 2
        beta = Pessoa('Ermac', 39, alfa.nome)
        print(beta.__dict__)
    """

# todo CURSO: Python Birds / AULA: Composição

"/home/lucas/PycharmProjects/recursos/PYTHON/POO/composicao.py"

# todo CURSO: Python Birds / AULA: Fase e Atores

def modulo_fase_classe_fase():
    """
    class Fase():
        def __init__(self, intervalo_de_colisao=1):
            self.intervalo_de_colisao = intervalo_de_colisao
            self._passaros = []
            self._porcos = []
            self._obstaculos = []
    """

# Adicionando imagens à placa gráfica (atores e objetos)
def modulo_fase():
    """
    def adicionar_obstaculo(self, *obstaculos):
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        self._passaros.extend(passaros)
    """

# todo CURSO: Python Birds / AULA: Sobrescrita de Atributo

def atores_py():
    """
    class Obstaculo(Ator):
    _carater_ativo = 'O'

    class Porco(Ator):
        _carater_ativo = '@'

    class PassaroVermelho(Passaro):
        _carater_ativo = 'V'
    """

# todo CURSO: Python Birds / AULA: Tipos de Teste

def tipos():
    """
    testes unitários (unittest)
    testes integrados ()
    """

"raiz / dir testes / fase_testes.py"
def fase_testes_py():
    """
    def teste_acabou_sem_porcos(self):
        fase = Fase()
        self.assertEqual(VITORIA, fase.status())
    """
    #  Esse método de teste contendo um erro proposital. Segurar o ctrl e clicar em [ status() ] de [ fase.status() ]


"raiz / fase.py"
def fase_py():
    """
        def status(self):
            return EM_ANDAMENTO
    """
    # Correção do método
    "return VITORIA"  # valor modificado na função [ status ], pois, se o jogo acabou sem porcos, então é: VITÓRIA

# todo CURSO: Python Birds / AULA: Método Protegido

"raiz / dir testes / fase_testes.py"
def fase_testes_py2():
    """
    def teste_acabou_com_porcos_e_passaros(self):
        fase = Fase()
        porcos = [PorcoFake(1, 1) for _ in range(2)]      # criando 2 porcos
        passaros = [PassaroFake(1, 1) for _ in range(2)]  # criando 2 pássaros
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)

        self.assertEqual(EM_ANDAMENTO, fase.status())  # EM_ANDAMENTO = há pássaros e porcos

        for ator in porcos + passaros:                 # concatenação de listas
            ator.status = DESTRUIDO                    # modificar cada índice para ter atributo de classe: DESTRUIDO
        self.assertEqual(VITORIA, fase.status())       # VITORIA = 'não há porcos ou há pássaros e não há porcos'

        fase.adicionar_obstaculo(Obstaculo())
        self.assertEqual(VITORIA, fase.status(),
                         'Obstáculo não interfere no fim do jogo')

        fase.adicionar_porco(PorcoFake())  # adicionando um porco, há porcos e não há pássaros, portanto = DERROTA
        self.assertEqual(DERROTA, fase.status(),
                         'Com Porco ativo e sem pássaro para lançar, o jogo '
                         'deveria acabar')

        fase.adicionar_passaro(PassaroFake())  # adicionando um pássaro, há porcos e pássaros, portanto = EM_ANDAMENTO
        self.assertEqual(EM_ANDAMENTO, fase.status(),
                         'Com Porco ativo e com pássaro para lançar, o jogo '
                         'não deveria acabar')
    """

"raiz / fase.py"
def fase_py2():
    """
    def status(self):
        if not self.possui_porco_ativo():
            return VITORIA
        elif self.possui_passaro_ativo():
            return EM_ANDAMENTO
        else:
            return DERROTA
    """
    # Os métodos chamados não existem, eles serão criados

"raiz / fase.py"  # métodos novos adicionados
def fase_py3():
    """
    def _possui_porco_ativo(self):
        for porco in self._porcos:
            if porco.status == ATIVO:
                return True
        return False

    def _possui_passaro_ativo(self):
        for passaro in self._passaros:
            if passaro.status == ATIVO:
                return True
        return False
    """
