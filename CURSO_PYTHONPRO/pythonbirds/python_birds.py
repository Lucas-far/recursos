

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

# todo CURSO: Python Birds / AULA: Classe

def projeto():
    """
    raiz / new / python package / poo
    poo / new / python file / pessoa.py
    """

# pessoa.py / Pessoa
def classe():
    """
    class Pessoa:
        pass
    """

# todo CURSO: Python Birds / AULA: Commit e Push

def criar_commit_local():
    """
    Criar commits
    --------------------------------
    raiz / botão direito / git / commit directory...
    --------------------------------

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