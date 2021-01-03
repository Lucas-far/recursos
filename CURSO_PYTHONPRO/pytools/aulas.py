

"""
Módulo >>> aulas.py

Objetivo:
         transcrever aulas do curso e sintetizar coisas relevantes
"""

#######################################################################################################################
"Pytools - Criação de Repositório"
#######################################################################################################################
def script():
    """
    1. https://github.com/
    2. +                  || canto superior direito da tela, próximo ao avatar
    3. New repository     || link do menu dropdown para iniciar a criação de um repositório
    4. Owner              || pode ser uma pessoa ou organização
    5. Description        || descrição do repositório
    6. Tipo               || repositórios costumam ser configurados como: PUBLIC
    7. README.md          || módulo que serve como documentação de explicação do projeto (linguagem markdown)
    8. .gitignore         || escolher sua linguagem de programação
    9. License            || normalmente, é do tipo: agpl (GNU Affero General Public License)
    10. Create repository || botão para criar um repositório
    """





#######################################################################################################################
"Pytools - Chaves SSH"
#######################################################################################################################
"5"  # ao executar, cria-se um dir em /home/user/nome_do_rep"
def git_clonar():
    """
    1 - Uma vez criado um repositório, este passa a ter um link: (https) ou (ssh)
    2 - No segundo caso, é preciso criar uma chave (explicado posteriormente)
    3 - O link de acesso encontra-se no botão (code)
    4 - Copia-se esse link
    5 - [ OPÇÃO 1 ] git clone link html ou ssh
    5 - [ OPÇÃO 2 ] git clone link html ou ssh nome do rep.
    """

"1"  # Ao executar, se for a primeira vez, será requisitado o login da sua conta GitHub
def git_logar():
    """
    1 - [ OPÇÃO 1 ] git push
    1 - [ OPÇÃO 2 ] git push origin master
    2 - Fornecer dados da sua conta Github
    """

"OBS"  # Essa etapa é feita para gerar no seu OS, um dir que contém sua chave SSH, para poder usá-la na sua conta GitHub
"OBS"  # A intenção de usar uma chave SSH, é para evitar requisições repetitivas de senha ao fazer commit
def git_gerar_ssh():
    """
    1 - [ Ubuntu  ] ssh-keygen -t rsa
    1 - [ Windows ] ssh-keygen.exe -t rsa
    2 - Apertar ENTER
    3 - Em seguida, será requisitado uma passphrase

       EXEMPLO:
               umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada

    4 - Apertar ENTER
    5 - Serão criados: (public key) (key fingerprint = SHA256) (key's randomart)
    6 - Acessar seu avatar no site do Github (canto superior direito da tela)
    7 - Dropdown (Settings)
    8 - Botão (SSH and GPG keys)
    9 - Botão (New ssh key)
    10 - Na página de criação da chave, temos: (title) (key)
    11 - Ir para: [ /home/seu_user/.ssh ]
    12 - Procurar: [ cat id_rsa.pub ]
    13 - Abrir e copiar a chave

    VIA TERMINAL:
                 11 até 13 - cd /home/seu_user/.ssh >>> cat id_rsa.pub >>> copiar retorno

    14 - Retornar à página de criação da chave SSH
    15 - Colar a chave copiada no campo: [ key ]
    16 - Salvar
    17 - Agora, você estará apto a clonar repositórios por sua chave SSH [ ver def git_clonar() ]
    """





#######################################################################################################################
"Pytools - Fork"
#######################################################################################################################
"1"  # Há diferença entre CLONE e FORK?
"2"  # O que seria CLONE?
"3"  # O que seria FORK?
"4"  # Como FORK conecta-se com o projeto original?
"5"  # Como CLONE conecta-se com o projeto original?
"6"  # Há algum padrão envolvendo CLONE e FORK?

"1"  # sim
"2"  # Copiar um projeto de um repositório, para enviá-lo para sua máquina, sem gerar uma cópia na sua conta Github
"3"  # Copiar um projeto de um repositório como um repositório novo na sua conta Github
"4"  # Através de um PULL REQUEST, que é enviado ao autor original, e avaliado se a mudança será efetuada
"5"  # Se você possui a chave SSH do repositório do projeto, a mudança já acontece através do COMMIT/PUSH
"6"  # Se for um repositório alheio, primeiro executa-se FORK, depois CLONE (html) ou (ssh). Pycharm [ get from VCS ]





#######################################################################################################################
"Pytools - Pull Request Não Aceito"
#######################################################################################################################
def linguagem_markdown():
    """
    1. Adicionar título para link: [título]
    2. Adicionar o link: (link)
    """

# Menu no GitHub para registrar possíveis erros em um projeto, normalmente quando há um grupo de pessoas envolvidas
def github_menu_issues():
    """
    1 - Ao acessar a página de issues, e posta-se uma, esta gera um id
    2 - Esse id especificado, pode ser mencionado em IDE's (contexto: Pycharm)
    3 - No console do commit, o id da issue é chamada pela sintaxe: [ close #id ]
    4 - Após o COMMIT/PUSH, requisita-se uma PULL REQUEST no GitHub
    5 - No post do PULL REQUEST, pode-se mencionar a sintaxe novamente: [ close #id ]
    """





#######################################################################################################################
"Pytools - Feature Branch"
#######################################################################################################################
"Breach"  # Ramos de códigos distintos a partir de um ponto no seu histórico
"Tipos"   # LOCAL BRANCH (projeto) (master ou origin/master) / REMOTE BRANCH (GitHub) (origin/master)
"Acesso"  # No Pycharm: [ Git / Branches... ] ou canto inferior direito da tela da IDE

def branch_comandos():
    """
    listar todas branches locais                                   [ git branch ]
    listar todas branches, incluindo remotas                       [ git branch --all ]
    listar todos repositórios remotos conectados                   [ git remote -v ]
    conectar um repositório remoto                                 [ git remote add ] <apelido> <link do rep.>
    desconectar um repositório remoto                              [ git remote rm    ] <apelido>
    atualizar todas as branches remotas de todos rep. remotos      [ git fetch --all ]
    atualizar todas as branches remotas de determinado rep. remoto [ git fetch ] <repositorio>
    criar uma branch local                                         [ git branch ] <nome-da-branch>
    carregar os módulos de uma branch especifica                   [ git checkout <nome-da-branch> ]
    """

def branch_comandos_executados():
    """
    [ Git / Manage Remotes... ]          # conectar um repositório remoto (Pycharm)
    [ Git / Fetch ]                      # atualizar todas as branches remotas de todos rep. remotos (Pycharm)
    [ Git / Branches... / + New branch ] # criar uma branch local (Pycharm)
    [ Git / Show Git Log ]               # verificar logs de braches feitas
    """





#######################################################################################################################
"Pytools - Arquivo Gitignore"
#######################################################################################################################
def criar_modulo():
    """
    1 - Ir a rota:    [ /home/user/ ]
    2 - Criar módulo: [ .gitignore_global ]
    3 - No módulo:
                  .idea/
                  bin/
                  *.sqlite3
    4 - No terminal:
                    git config --global core.excludesfile ~/.gitignore_global
    """





#######################################################################################################################
"Pytools - Pyenv no Ubuntu"
#######################################################################################################################
"Sobre"  # Comandos relevantes para ter uma configuração completa para Python no OS Ubuntu
def terminal():
    """
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev
    """

def instalar_pyenv():
    """
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    """

"Bashrc"  # Configurar binários do Pyenv para ele ser reconhecido pelo OS no terminal
def bashrc():
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
    """

def atualizar():
    """
    1 - pyenv install -l
    2 - Procurar na listagem, a versão inteiramente numérica mais atual
        EXEMPLO:
                3.9.1
    2 - pyenv install 3.9.1
    """
