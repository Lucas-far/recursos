

# Softwares: 1. Java development kit (oracle) / 2. Python / 3. Pycharm
def softwares():
    """
    1. 04-jdk-11.0.7_linux-x64_bin.tar.gz
       FONTES:
              Google = Java Archive Downloads - Java SE 11 - Oracle
              https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html

    2. python-3.8.5.tar.xz
       FONTES:
              https://www.python.org/downloads/ (Site / Downloads / All releases)

    3. pycharm-community-2020.2.tar.gz
    4. CONTA ORACLE: [ lu******2@g****.com ] [ W******s17 ]
    """

def configurar_java():
    """
    1. Extrair o módulo compilado java baixado no mesmo local onde ele está [ Extract here ]
    2. Renomear o diretório para [ jdk11 ]
    3. Se em [ jdk11 ] há módulos aninhados, leve todos para o diretório matriz
    4. Recortar (ctrl + x) o diretório [ jdk11 ]
    5. /home/meu_user/apps (se não existe, criar este diretório)
    6. Colar (ctrl + v) o diretório [ jdk11 ] em /home/meu_user/apps
    7. Retornar um nível [ /home/meu_user ]
    8. ctrl + h (para mostrar módulos ocultos)
    9. Procurar e abrir [ .bashrc ]
    10. Vá ao final do módulo e adicione as seguintes linhas de código:

        JAVA_HOME=/home/meu_user/apps/jdk11
        export JAVA_HOME
        PATH=$PATH:$JAVA_HOME/bin
        export PATH

    11. Ir ao terminal, e checar se o Java foi instalado: [ java --version ]
    12. Se há um retorno da versão do Java, então teve sucesso
    """

# Atualizam-se os pacotes do Ubuntu
def terminal():
    """ sudo apt-get update """

# É recomendável outras ferramentas essenciais
def terminal2():
    """
    sudo apt install build-essential curl libbz2-dev libffi-dev libgdbm-dev libjpeg-dev liblzma-dev libncurses5-dev
    libnss3-dev libreadline-dev libsqlite3-dev libssl-dev sqlite3 zlib1g-dev
    """

def configurar_python():
    """
    1. Extrair o módulo compilado python baixado no mesmo local onde ele está [ Extract here ]
    2. Entrar na pasta extraida do Python
    3. botão direito >>> open in terminal

       TERMINAL:
                1. ./configure --enable-optimizations --with-ensurepip=install
                2. make -j 2
                3. sudo make altinstall
                4. python 3 --version / python3.8 --version
                5. pip3.8 --version
                6. sudo pip3.8 install --upgrade pip
                7. sudo pip3.8 install virtualenv virtualenvwrapper

    5. Ir para para /home/meu_user
    6. ctrl + h (para mostrar módulos ocultos)
    7. Procurar e abrir [ .bashrc ]
    8. Vá ao final do módulo e adicione as seguintes linhas de código:

       export WORKON_HOME=$HOME/.virtualenvs
       export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.8  # terminal: which python3.8
       source /usr/local/bin/virtualenvwrapper.sh
    """

# Com o virtualenv instalado, é preciso conhecer alguns comandos essenciais
def terminal3():
    """
    mkvirtualenv nome do av   # criação e login em um av
    deactivate                # deslogar de um av criado
    work on nome do av        # relogar em um av criado
    rmvirtualenv nome do av   # remover um av especificado
    """

def configurar_pycharm():
    """
    1. Extrair o módulo compilado pycharm baixado no mesmo local onde ele está [ Extract here ]
    2. Renomear o diretório para [ pycharm ]
    3. /home/meu_user/apps (se não existe, criar este diretório)
    4. Recortar (ctrl + x) o diretório [ pycharm ] para [ /home/meu_user/apps/ ]
    5. Entrar no diretório [ pycharm/bin ]
    6. botão direito >>> open in terminal

    7. TERMINAL:
                sudo apt-get install alacarte -y

    8. Agora é melhor que seja configurado um ícone para o software, para melhor acesso
    9. Ir ao Desktop, em [ Show applications ]
    10. Procurar e abrir [ Main Menu ]
    11. [ Applications / Programming ]
    12. [ New item ] [ Name: Pycharm ] [ Command: /home/apps/pycharm/bin/pycharm.sh ]
    13. Adicionar um ícone: [ /home/lucas/apps/pycharm/bin/pycharm.png ]
    """

# Configuração essencial para criar projetos no Pycharm
def pycharm():
    """
    1. Abrir o software
    2. Clicar em [ New Project ]
    3. Há duas formas de criar um projeto novo

       FORMA 1: Quando um ambiente não foi criado usando o comando: [ mkvirtualenv ]

       1. Location = rota/nome do av
       2. New environment
              Base Interpreter
                  ...
                      /usr/local/bin/python3.8

       FORMA 2: Quando um ambiente já foi criado usando o comando: [ mkvirtualenv ]

       1. Location = rota/nome do av
       2. Existing Interpreter
              ...
                  Add Python Interpreter
                      /usr/bin/python3.8
    """
