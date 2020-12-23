

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

def exemplo():
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

"Módulo"  # fase.py
"Local"   # raiz
"Função"  # def __init__
def fase_py():
    """
    class Fase():
        def __init__(self, intervalo_de_colisao=1):
            self.intervalo_de_colisao = intervalo_de_colisao
            self._passaros = []
            self._porcos = []
            self._obstaculos = []
    """

"Módulo"    # fase.py
"Local"     # raiz
"Função"    # def adicionar_obstaculo / def adicionar_porco / def adicionar_passaro
"Objetivo"  # Adição de imagens à placa gráfica (atores e objetos)
def fase_py2():
    """
    def adicionar_obstaculo(self, *obstaculos):
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        self._passaros.extend(passaros)
    """

# todo CURSO: Python Birds / AULA: Sobrescrita de Atributo

"Módulo"    # atores.py
"Local"     # raiz
"Classe"    # Obstaculo / Porco / PassaroVermelho
"Objetivo"  # alterar variável _carater_ativo
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

"Módulo"    # fase.py
"Local"     # raiz
"Função"    # def status
"Objetivo"  # correção do retorno do método, pois, se o jogo acabou sem porcos, então é: VITÓRIA
def fase_py3():
    """
    def status(self):
        return VITORIA
    """

"Módulo"    # fase_testes.py
"Local"     # raiz/testes
"Função"    # def teste_acabou_sem_porcos
"Objetivo"  # teste do método para saber se ele passa...................................................................

# todo CURSO: Python Birds / AULA: Método Protegido

"Módulo"  # fase.py
"Local"   # raiz
"Função"  # def _possui_porco_ativo / def _possui_passaro_ativo (criados)
def fase_py4():
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

"Módulo"  # fase.py
"Local"   # raiz
"Função"  # def status
def fase_py5():
    """
    def status(self):
        if not self.possui_porco_ativo():
            return VITORIA
        elif self.possui_passaro_ativo():
            return EM_ANDAMENTO
        else:
            return DERROTA
    """

"Módulo"    # fase_testes.py
"Local"     # raiz/testes
"Função"    # def teste_acabou_com_porcos_e_passaros
"Objetivo"  # teste do método para saber se ele passa...................................................................

# todo CURSO: Python Birds / AULA: Ciclo de Vida de Objetos

"Módulo"  # fase.py
"Local"   # raiz
"Função"  # def lancar
def fase_py6():
    """
    def lancar(self, angulo, tempo):
        for passaro in self._passaros:
        if not passaro.foi_lancado():
            passaro.lancar(angulo, tempo)
            break
    """

"Módulo"    # fase_testes.py
"Local"     # raiz/testes
"Função"    # def teste_lancar_passaro_sem_erro_quando_nao_existe_passaro
"Objetivo"  # teste do método para saber se ele passa...................................................................

# todo CURSO: Python Birds / AULA: Fase Completa

"Módulo"  # fase.py
"Local"   # raiz
"Função"  # class Fase / def calcular_pontos
def fase_py7():
    """
    def calcular_pontos(self, tempo):
        for passaro in self._passaros:
            passaro.calcular_posicao(tempo)
            for alvo in self._obstaculos + self._porcos:
                passaro.colidir(alvo, self.intervalo_de_colisao)
            passaro.colidir_com_chao()
        pontos = [self._transformar_em_ponto(a) for a in self._passaros+self._obstaculos+self._porcos]

        return pontos
    """

"Módulo"    # fase_testes.py
"Local"     # raiz/testes
"Função"    # def teste_intervalo_de_colisao_padrao
"Objetivo"  # teste do método para saber se ele passa...................................................................

"Módulo"    # fase_testes.py
"Local"     # raiz/testes
"Função"    # def teste_intervalo_de_colisao_nao_padrao
"Objetivo"  # teste do método para saber se ele passa...................................................................

# todo CURSO: Python Birds / AULA: Posição de Ator

"Módulo"    # atores.py
"Local"     # raiz
"Função"    # class Ator / def calcular_posicao
def atores_py2():
    """
    def calcular_posicao(self, tempo):
        return self.x, self.y
    """

"Módulo"    # atores_testes.py
"Local"     # raiz/testes
"Função"    # class AtorTestes / def teste_ator_posicao
"Objetivo"  # teste do método para saber se ele passa...................................................................
