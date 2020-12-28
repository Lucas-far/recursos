

""""""
# todo CURSO: Pytools / AULA: Criação de Repositório
def criar_repositorio():
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





# todo CURSO: Pytools / AULA: Chaves SSH
"TERMINAL - ao executar, cria-se um dir em /home/user/, por padrão, com o nome do próprio repositório"
def git_clonar():
    """
    1. Uma vez criado um repositório, este passa a ter um link: (https) ou (ssh)
    2. No segundo caso, é preciso criar uma chave (explicado posteriormente)
    3. O link de acesso encontra-se no botão (code)
    4. Copia-se esse link
    5. TERMINAL -> [ git clone link html ou ssh ] ou [ git clone link html ou ssh nome do rep. ]
    """

"TERMINAL - ao executar, se for a 1a vez, será requisitado um login"
def git_logar():
    """
    1. TERMINAL: [ git push ] ou [ git push origin master ]
    2. Entra-se com os dados da sua conta Github
    """

"TERMINAL - a fim de tornar o comando de push independente de passar a senha em loop, cria-se uma chave SSH"
def git_gerar_ssh():
    """
    1. TERMINAL: [ ssh-keygen -t rsa ] (Linux) [ ssh-keygen.exe -t rsa ] (Windows)
    2. Uma rota padrão é sugerida, para inserir os diretórios e módulos onde chaves (privada) & (pública) serão salvas
    3. Apertar ENTER
    4. Em seguida, será requisitado uma passphrase, que é uma senha, e é reincidente

       EXEMPLO:
               umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada

    4. Apertar ENTER
    5. Serão criados: (public key) (key fingerprint = SHA256) (key's randomart)
    6. Dirija-se ao seu avatar no site do Github (canto superior direito da tela)
    6. Dropdown (Settings)
    7. Selecionar: (SSH and GPG keys)
    8. Selecionar: (New ssh key)
    9. Na página de criação da chave, temos: (title) (key)
    10. Duas formas de acessar a chave:

        FORMA 1:
                cd .ssh -> cat id_rsa.pub -> ctrl + c -> voltar à página de criação da chave ssh -> ctrl + v
        FORMA 2:
                ir manualmente ao dir, e copiar manualmente

    11. Clicar: (Add ssh key)
    12. A partir desse momento, você poderá clonar repositórios pelo (ssh) [ ver def git_clonar() ]
    """





# todo CURSO: Pytools / AULA: Fork
"Há diferença entre CLONE e FORK?"  # sim

"O que seria CLONE?"
# Copiar um projeto de um repositório, para enviá-lo para sua máquina, sem gerar uma cópia na sua conta Github

"O que seria FORK?"
# Copiar um projeto de um repositório como um repositório novo na sua conta Github

"Como FORK conecta-se com o projeto original?"
# Através de um PULL REQUEST, que é enviado ao autor original, e avaliado se a mudança será efetuada

"Como CLONE conecta-se com o projeto original?"
# Se você possui a chave de acesso (SSH), a mudança feita por você, já acontece através do PUSH

"Há algum padrão envolvendo CLONE e FORK?"
# Se for um repositório estrangeiro, primeiro executa-se FORK, depois CLONE (html) ou (ssh). Pycharm [ get from VCS ]



# todo CURSO: Pytools / AULA: Pull Request Não Aceito
def linguagem_markdown():
    """
    1. Adicionar título para link: [título]
    2. Adicionar o link: (link)
    """

def github_menu_issues():
    """
    Objetivo:
             criar tópicos, no Github, para informar sobre problemas
    OBS:
        1. cada issue possui sua id, e esta pode ser inserida na mensagem do commit, pela sintaxe: [ close #id ]
        2. ao executar o COMMIT/PUSH, requisita-se uma PULL REQUEST
        3. na tela do PULL REQUEST, pode-se mencionar a sintaxe [ close #id ]
    """





# todo CURSO: Pytools / AULA: Feature Branch
def branch_conceito():
    """ Ramos de códigos distintos a partir de um ponto no seu histórico """

def branch_tipos():
    """
    Ramo local  (local branch)  -> ramo interno ao seu projeto
    Ramo remoto (remote branch) -> ramo externo ao seu projeto
    """

def branch_pycharm():
    """
    Representação         || galhos com pontos nas extremidades
    Localização           || canto inferior direito da tela da IDE
    Nome da branch local  || master ou origin/master
    Nome da branch remota || origin/master
    """

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
    conectar um repositório remoto (Pycharm)                            [ menu=git / opção=manage remotes ]
    atualizar todas as branches remotas de todos rep. remotos (Pycharm) [ menu=git / opção=fetch ]
    criar uma branch local (Pycharm)                                    [ canto inferior direito / + new branch ]
    verificar logs de braches feitas                                    [ canto inferior esquerdo / git / log ]
    """





# todo CURSO: Pytools / AULA: Arquivo Gitignore
def criar_modulo():
    """
    Local           || /home/user/
    Nome            || .gitignore_global
    Conteúdo ('\n') || .idea/ bin/ *.sqlite3
    TERMINAL        || git config --global core.excludesfile ~/.gitignore_global
    """
