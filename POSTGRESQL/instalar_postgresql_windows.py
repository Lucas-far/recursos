

"""
Objetivo:
         configurar bdd postgresql para poder usar em projetos Django no OS Windows
"""

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 8:PostgreSQL - Parte 1
    Aula  # 74. Instalação e Configuração no Windows
    """

def software():
    """
    Baixar e instalar software PostgreSQL x64 para OS Windows
        https://www.postgresql.org/download/windows/
    """

# Ferramentas no instalador, a serem baixadas
def instalar_mysql():
    """
    1. PostgreSQL server
    2. Pgadmin4
    3. Stack Builder
    4. Command line tools
    5. Também será requisitado a configuração de uma senha para o usuário admin padrão [ postgres ]
    """
    # 3. Software que disponibiliza mais ferramentas para PostgreSQL

# Configuração do software - PARTE 1
def registrar_postgresql_bin():
    """
    1. Ir à rota padrão de instalação do postgresql no Windows, na pasta bin
       ROTA (copiar) (ctrl + c):
                                c:\Program Files\PostgreSQL\12\bin

    2. No windows, seguir os seguinte passos:
       Win
           este computador = pesquisar
                botão direito
                    propriedades
                        configurações avançadas do sistema
                            variáveis de ambiente
                                path
                                    editar
                                        novo

    3. Colar a rota da pasta binária:
                                     c:\Program Files\PostgreSQL\12\bin
    """

def terminal():
    """
    1. psql -U postgres
    2. Inserir senha do usuário admin [ postgres ]
    3. O terminal retornará o Console psql

    OBSERVAÇÕES:
                4. Porém a melhor maneira de uso do PostgresSQL é pela sua aplicação web [ Pgadmin4 ]
                5. Pgadmin4 é instalado durante a instalação do software postgresql
    """

# Configuração do software - PARTE 2
def pgadmin4_parte1():
    """
    1. Abrir o software [ Pgadmin4 ]
    2. Na abertura, sempre será requisitado a senha da sua conta Windows

    3. Ao fornecer a senha criada:
       Servers
           PostgreSQL12
               digitar senha = usuário [ postgres ] da instalação
    """

# Criação do usuário novo, apartir do padrão [ postgres ]
def pgadmin4_parte2():
    """
    1. Após as duas requisições, torna-se disponível:
       Login/Group Roles
           botão direito
               create
                   login/group role...
                       general
                           name = nome do usuário novo
                               definition
                                   password = senha do usuário novo
                                       privilegies
                                           Can login = Yes
                                               Superuser = Yes
                                                   save
    """

# Configuração do servidor novo, não padrão
def pgadmin4_parte3():
    """
    ALTERNATIVO: deletar servidor padrão

        Browser
            Servers
                PostgreSQL 12
                    botão direito
                        remove server
                            yes

    CRIAÇÃO DE UM SERVIDOR NOVO

        Browser
            Servers
                botão direito
                    Create
                        Server
                            General
                                name = dê um nome ao servidor
                                    Connection
                                        host = localhost
                                        username = nome do usuário criado em [ Login/Group Role... ]
                                        password = senha do usuário criado em [ Login/Group Role... ]
                                            save
    """
