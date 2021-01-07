

"""
Módulo >>> abrir_projeto_estrangeiro_github.py

Objetivo:
         mostrar um procedimento padrão para utilizar um projeto estrangeiro do Github para uma máquina local, caso o
         projeto possua módulos como: [ gitignore / license / readme.md ]

         CASO CONTRÁRIO:
                        1 - executar os passos dos métodos [ def github ] e [ def github2 ]
"""

# Condições para quando um projeto possuir módulos relevantes ausentes
def github():
    """
    1 - Menu - Your repositories - New
    2 - Preencher os dados e criar um repositório (de preferência, privado)
    3 - A partir desse momento, haverá um repositório simples criado, contendo os módulos necessários
    4 - Pode-se continuar com o tutorial
    5 - Porém, ao final do mesmo, alguns outros procedimentos criados aqui, serão necessários
    """

def tutorial():
    """
    1 - Acessar o repositório a ser clonado
        ===== https://github.com/Lucas-far/attempt_api =====

    2 - Copiar o repositório alvo:
        ===== Code / HTTPS / copiar =====

    3 - Abrir o Pycharm e procurar por [ Get from VCS ]

    4 - Preencher os dados: URL (o link do rep) e Directory (local e nome do projeto)
        ===== URL: https://github.com/Lucas-far/attempt_api.git    =====
        ===== Directory: /home/lucas/PycharmProjects/attempt_api_2 =====

    5 - Ao fazer isso, um projeto novo é criado e aberto, com os módulos do repositório clonado

    6 - Instalar um ambiente virtual (presumindo que já tenha instalado no OS):
        ===== python3 -m venv .venv =====

    7 - Ativar o ambiente virtual instalado
        ===== source .venv/bin/activate =====

    8 - Escolher interpretador python existente de dentro da pasta do ambiente virtual

        OPÇÃO 1
        ===== File / Settings / pesquisar: Interpreter / engrenagem =====
        ===== .venv/bin/python                                      =====

        OPÇÃO 2
        ===== No canto inferior direito do Pycharm, há a opção de escolher o interpretador =====
        ===== Ao clicar, escolher a opção: [ Add interpreter ]                             =====
        ===== .venv/bin/python                                                             =====

    9 - Instalar os dependências (se há):
        ===== pip install -r requirements.txt =====

    11 - Executar comandos
         ===== python manage.py migrate   =====
         ===== python manage.py runserver =====
    """

def github2():
    """
    1 - Retornar à página do Github, abrir cada um dos módulos e copie seu conteúdo
    2 - Volte ao projeto já clonado e crie módulos com o mesmo nome e o mesmo conteúdo
    3 - Dai então, a configuração estará completada
    """
