

"""
Objetivo:
         utilizar bdd postgresql para poder usar em projetos Django no OS Ubuntu

Palavra chave >>> instalar postgresql
"""

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 8:PostgreSQL - Parte 1
    Aula  # 75. Instalação e Configuração no Linux
    """

def terminal():
    """
    sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    sudo reboot
    """

# https://www.postgresql.org/download/linux/ubuntu/
def instalar_parte1():
    """
    1 - sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    2 - wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    3 - sudo apt-get update
    4 - sudo apt-get -y install postgresql-13

        COMANDO QUE PODE APARECER DURANTE A INSTALAÇÃO:
        4.1 - pg_ctlcluster 13 main start
    """

def comandos_condicionais():
    """
    Se após os 3 comandos anteriores, haver um erro de arquitetura [ i386 ], então fazer os códigos

    Se   [ dpkg --print-foreign-architectures ] == i386, então continuar
    Se   [ dpkg --print-architecture ]          == amd64, então continuar
    Usar [ sudo dpkg --remove-architecture i386 ]
    """

def instalar_parte2():
    """
    sudo apt-get -y install postgresql-12 (já há a versão 13)
    sudo apt-get -y install pgadmin4
    """

def terminal2():
    """
    sudo su - postgres  # logar no postgresql com a conta padrão admin [ postgres ]
    psql                # usar o console psql em uma conta já logado [ no contexto: postgres ]
    help                # buscar comandos auxiliares
    \q                  # deslogar a conta
    exit                # deslogar do postgresql
    """

# Configurar uma senha para o usuário padrão [ postgres ]
def terminal3():
    """
    1 - sudo su - postgres
    2 - psql
    2. ALTER user postgres WITH PASSWORD 'senha desejada';
    3. \q
    4. exit
    """
    # 2. retorno = ALTER ROLE

# Configurar um novo usuário, apartir do padrão [ postgres ]
def terminal4():
    """
    1 - sudo su - postgres
    2 - psql
    3 - CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    4 - ALTER USER nome do usuário novo WITH SUPERUSER;
    5 - \q
    6 - exit
    """

# Tutorial: como usar PgAdmin4
def pgadmin4():
    """
    1. PgAdmin4 é um software gerenciador para bdds do postgresql

    2. TERMINAL:
                sudo apt-get -y install pgadmin4

    3. CRIAR UM SERVIDOR PARA CADA CONTA NOVA
       Servers
           botão direito
               create
                   server
                       general
                           name = dê um nome ao servidor
                               connection
                                   host = localhost
                                       username = nome do usuário novo criado
                                           password = senha do usuário novo criado

    4. APÓS CRIAR UM SERVIDOR, ESTE PODE TER VÁRIOS BDDS, UM PARA CADA PROJETO
       Servidor (abaixo dele, há a opção: databases)
           databases
               botão direito
                   create
                       database
                           database = dê um nome ao bdd
                               save
    """

# Deletar usuário não postgres
def tutorial():
    """
    1 - sudo su - postgres
    2 - dropuser nome_do_usuário
    :return:
    """

# Deletar postgresql
def tutorial2():
    """
    1 - sudo apt-get --purge remove postgresql
    2 - dpkg -l | grep postgres
    3 - sudo apt-get --purge remove

    pgdg-keyring
    postgresql-12
    postgresql-13
    postgresql-client-12
    postgresql-client-13
    postgresql-client-common
    postgresql-common

    4 - sudo apt-get --purge remove postgresql-12 postgresql-13 postgresql-client-12 postgresql-client-13 postgresql-client-common postgresql-common
    """
