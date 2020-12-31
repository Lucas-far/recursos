

"""
Objetivo:
         instalar MySQL para poder usar em projetos Django

Contas atuais:
              lu***dm**  / *as****t2*7*
              lu***dm**2 / *as****t2*7*
"""

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 6:MySQL - Parte 1
    Aula  # 45. Instalação e Configuração no Linux
    """

# Comandos de atualização no OS Ubuntu
def terminal():
    """
    sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    sudo reboot
    """

# Comando para instalar o servidor MySQL
def terminal2():
    """
    sudo apt install mysql-server
    """

# Comandos pós instalação do MySQL
def terminal3():
    """
    1 - sudo mysql                    #  Logar no console MySQL
    2 - help                          #  Lista de comandos do console MySQL
    3 - exit                          #  Sair do console MySQL

    4 - sudo systemctl status mysql   #  Verificar status do servidor mysql pós sua instalação
    5 - sudo systemctl enable mysql   #  Iniciar servidor MySQL com o sistema operacional
    6 - sudo systemctl disable mysql  #  Cancelar iniciar o servidor MySQL com o sistema operacional
    7 - sudo systemctl start mysql    #  Iniciar/reiniciar servidor MySQL
    8 - sudo systemctl stop mysql     #  Congelar servidor MySQL
    """
    # 2 e 3 são dependentes de 1
    # 4 adiante, são indepentes

# Configurar um servidor MySQL
def terminal4():
    """
    1 - sudo mysql_secure_installation

    OBSERVAÇÃO:
               serão executadas perguntas sobre ferramentas, algumas para adicionar, outras para remover

    Validate Password Plugin  # Digitar 'y' ou 'n'
    Password                  # Digitar uma senha para o usuário 'root' do MySQL
    Remove Anonymous user     # Digitar 'y'
    Login remotely            # Digitar 'y'
    Remove Test database      # Digitar 'y' ou 'n'
    Reload Privilege tables   # Digitar 'y'
    """

# Criação do usuário novo apartir do usuário admin padrão
def terminal5():
    """
    1. sudo mysql
    2. SHOW VARIABLES LIKE 'validate_password%';
    3. SET GLOBAL validate_password.policy=LOW;
    2. CREATE USER 'nome do usuário'@'localhost' IDENTIFIED BY 'senha desejada';
    3. GRANT ALL PRIVILEGES ON *.* TO 'usuário criado'@'localhost' WITH GRANT OPTION;
    4. FLUSH PRIVILEGES;
    5. exit
    6. sudo mysql -unome do usuário novo -p
    7. digitar a senha do OS
    8. digitar a senha do usuário novo
    """
    # 3 - altera uma das linhas da tabela responsável pela segurança da senha para: LOW

# Comandos pós login de uma conta
def terminal6():
    """
    SHOW DATABASES;                  # Mostrar todos os bdds
    USE nome do bdd;                 # Acessar um bdd específico (se você está em outro bdd, ele será deslogado)
    SHOW TABLES;                     # Mostrar tabelas de um bdd (já estando logado em um bdd específico)
    SELECT * FROM tabela de um bdd;  # Consultar uma tabela específica
    SELECT * FROM sys_config;        # Exemplo do comando acima
    """

# todo...Importante (Instalação da ferramenta MySQL Workbench)

def download_mysql_workbench():
    """
    Google:
           MySQL Workbench - MySQL
    Link direto:
                https://www.mysql.com/products/workbench/
    Observação:
               é um instalador normal, como acontece no Windows, sem necessidade de configurações avançadas
    """
