

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

"/home/lucas/PycharmProjects/recursos/PYTHON/POO/exemplo_composicao.py"
