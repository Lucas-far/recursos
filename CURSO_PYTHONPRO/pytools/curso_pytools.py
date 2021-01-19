

"""
Módulo || curso_pytools.py
"""

###########################
"Pytools"  # Feature Branch
###########################



##############################
"Pytools"  # Arquivo Gitignore
##############################

"Título"  # Configuração de um módulo gitignore global
def parte1():
    """
    1 - [ /home/seu_user/ ] local recomendado para criar o módulo git
    2 - [ .gitignore_global ] recomendação de nome do módulo git
    3 - Conteúdo do módulo:
                           .idea/
                           bin/
                           *.sqlite3
    4 - No terminal:
                    git config --global core.excludesfile ~/.gitignore_global
    """

############################
"Pytools"  # Pyenv no Ubuntu
############################

"Título"  # Bibliotecas relevantes para ter uma configuração completa para Python no OS Ubuntu
def parte1():
    """
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev
    """

"Título"  # Instalação do Pyenv
"OBS"     # Pyenv instala Python no OS, sem afetar o Python existente no OS
def parte2():
    """
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    """

"Título"  # Configuração dos binários do Pyenv
def parte3():
    """
    1 - Ir à rota: [ /home/seu_user/.bashrc ]
    2 - Abrir o módulo
    3 - Inserir no final do módulo:
                                   export PATH="/home/lucas/.pyenv/bin:$PATH"
                                   eval "$(pyenv init -)"
                                   eval "$(pyenv virtualenv-init -)"
    4 - Salvar
    5 - Fechar o terminal
    6 - Reabrir o terminal
    7 - pyenv
    8 - Se a instalação teve êxito, o Pyenv será chamado no terminal
    9 - pyenv install -l
    10 - Procurar na listagem, a versão inteiramente numérica mais atual
        EXEMPLO:
                3.9.1
    11 - pyenv install 3.9.1
    """

#######################
"Pytools"  # Virtualenv
#######################

"Título"  # Objetivos para instalar o virtualenv para o Python
def parte1():
    """
    1 - Criar ambientes virtuais isolados no OS
    2 - Tratar projetos com versões diferentes do Python
    3 - Permitir que projetos tenham versões diferentes de library (projetos legado) (versões bem anteriores)
    """

###################
"Pytools"  # Flake8
###################
"FONTE"  # /home/lucas/PycharmProjects/recursos/PYTHON/f/flake8.py

##############################################
"Pytools"  # Integração Contínua com Travis CI
##############################################

def parte1():
    """
    1 - Travis é uma integração contínua (continuous integration) para evitar execução de tarefas manuais reincidentes
    2 - https://travis-ci.org/
    3 - Signup com sua conta GitHub [ https://travis-ci.org/getting_started / activate all repositories... (botão) ]
    4 - No projeto, criar um diretório: [ raiz / botão direito / new / file / .travis.yml ]
    5 - Configuração o módulo .yml para Python

        language:
          - Python
        version:
          - 3.8
        install:
          - pip install -r requirements.txt
        script:
          - flake8

    6 - Commit
    7 - Push
    8 - Ir ao Travis website
    9 - Ir ao repositório do projeto alvo
    10 - Atualizar a página
    11 - Verificar se o processo de build é executado
    """

####################################
"Pytools"  # Upgrade de Dependências
####################################

"Título"  # Instalação e utilização do Pyup
def parte1():
    """
    1 - Pyup mantêm as dependências de um projeto atualizadas
    2 - https://pyup.io/ -----> Signup pelo Github
    3 - Dar a permissão de acessar repositórios da conta
    4 - Adicionar repositório a ser checado
    5 - O repositório será checado e se haver dependências desatualizadas, estas serão mostradas no website do Pyup
    6 - Além da lista de dependências desatualizadas, serão criados PULL REQUESTS para fazê-las
    7 - Pyup também possuem badges (não funcionaram no momento desse tutorial)
    8 - Configurar módulo no projeto:

        raiz / new / file / .pyup.yml

    9 - Conteúdo do módulo:

        9.1 - Eu tentei de tudo e não consegui achar solução
        9.2 - O exemplo oficial da documentação não é apropriado para o meu contexto, pois não quero atualizar o Django
        9.3 - https://pyup.io/docs/bot/config/#specifying-files
        9.4 - https://pyup.io/docs/bot/filter/
        9.5 - Eu não consigo fazer os exemplos da documentação da ferramenta funcionar

    10 - Tendo as etapas 8 e 9 falhado para mim, a opção 5 ainda é uma realidade
    """

def parte2():
    """
    11 - Sendo assim, vê-se as dependências com badge "outdated" e copia-se o que está no cabeçalho "package"
    12 - Ir ao módulo [ requirements.txt ] e fazer [ ctrl + f ] para procurar
    13 - Colar e ir até a dependência selecionada
    14 - Copiar toda a dependência (incluindo a versão)
    15 - Executar: [ pip uninstall ctrl + v ]
    16 - Fazer isso com todas as dependências desatualizadas, separando-as cada uma por um espaço

         EXEMPLO:
                 pip unisinstall beautifulsoup4==4.9.3 django-bootstrap4==2.3.1 pyflakes==2.2.0

    17 - Antes de executar, copiar todas essas
    """

"OBS"  # Procedimentos para o módulo requirements.txt customizado e do projeto
"OBS"  # Começar da linha 1 e não deixar linhas sobrando ao final, para evitar problemas com leitura de módulos

# Módulo criado a partir de dados filtrados do website Pyup, e organizados em um módulo .txt
def parte3():
    """
    1 - Criar um módulo [ requirements.txt ]
    2 - https://pyup.io/account/repos/github/Lucas-far/attempt_api/

    3 - Copiar segurando (ctrl + botão esquerdo descendo) para selecionar cada <td></td> que seja do seu interesse
    3 - Copiar segurando (ctrl + botão esquerdo) para selecionar cada <td></td> que seja do seu interesse
    3 - Não é possível fazer o primeiro 3 duas vezes seguidas, por isso há o segundo 3

    4 - Colar dados selecionados no módulo .txt
    5 - Organizar os dados (mesmo layout do módulo requirements.txt de um projeto Django)
    6 - Salvar o módulo
    7 - Pegar a rota do módulo, pois essa será usada na parte 4
    """

# Módulo criado na raiz do projeto Django (pode ser deletado após a coleta dos resultados)
def parte4():
    """
    1 - Criar um módulo [ requirements.py ]
    2 - Eu criei um algoritmo me poupa o trabalho de desintalar e instalar as dependências manualmente
    3 - Para o funcionamento desse método, é preciso:

        rota do módulo requirements.txt do projeto (incluindo o módulo.formato)
        rota do módulo .txt (incluindo o módulo.formato)

    ALGORITMO

        def checar_dependencias(dependencia_projeto, dependencia_pyup):

            # Dependências atualmente no projeto
            with open(dependencia_projeto, 'r') as doc:
                var = sorted(list(str(doc.read()).split('\n')), reverse=True)

            # Dependências atualizadas do projeto, pegas do site Pyup e organizadas em um módulo .txt
            with open(dependencia_pyup, 'r') as doc:
                var2 = sorted(list(str(doc.read()).split('\n')), reverse=True)

            "OBS"  # sorted está sendo usado para ordenar dados para evitar possíveis irregularidades do projeto ou do website Pyup

            var3 = ['pip uninstall -y', ]  # lista de índices que receberá pacote desatualziado a ser desinstalado
            var4 = ['pip install', ]    # lista de índices que receberá cada pacote atualizado a ser instalado

            "Objetivo"  # Se var e var2 são iguais, não há o que atualizar, então apenas imprime-se 'OK' + incremento
            "Objetivo"  # Se não, adicionar em var3, o pacote a ser desintalado, e em var4, o pacote a ser instalado + incremento
            index = 0
            while index < len(var):
                if var[index] == var2[index]:
                    print('OK', end=' ')
                    index += 1
                else:
                    var3.append(var[index])
                    var4.append(var2[index])
                    index += 1

            print('\n')
            print('Pacotes desatualizados')
            for obj in var3:
                print(obj, end=' ')  # Copia-se o retorno dessa linha e execute ela no terminal do projeto

            print('\n')
            print('Pacotes atualizados')
            for obj in var4:
                print(obj, end=' ')  # Depois, copia-se o retorno dessa linha e execute ela no terminal do projeto

        checar_dependencias(
            '/home/lucas/PycharmProjects/attempt_api/requirements.txt',
            '/home/lucas/PycharmProjects/recursos/teste.txt'
        )
    """
