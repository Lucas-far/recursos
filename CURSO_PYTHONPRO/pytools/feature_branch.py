

"""
Módulo: Feature Branch

Aula          || Feature Branch
Palavra_chave || tutorial branch
Objetivo      ||
"""

"Breach"  # Ramos de códigos distintos a partir de um ponto no seu histórico
"Tipos"   # LOCAL BRANCH (projeto) [master ou origin/master]
"Tipos"   # REMOTE BRANCH (GitHub) [origin/master]
"Acesso"  # No Pycharm: [ Git / Branches... ] ou canto inferior direito da tela da IDE

# Comando para branch comuns
def parte1():
    """
    listar todas branches locais
        1 - git branch
        2 - menu -> git -> branches

    listar todas branches, incluindo remotas     [ git branch --all ]
    listar todos repositórios remotos conectados [ git remote -v ]

    conectar um repositório remoto
        1 - git remote add apelido link https ou ssh
        2 - menu -> git -> manage remotes -> name=apelido -> url=link SSH -> OK

    desconectar um repositório remoto                              [ git remote rm ] <apelido>
    atualizar todas as branches remotas de todos rep. remotos      [ git fetch --all ]
    atualizar todas as branches remotas de determinado rep. remoto [ git fetch ] <repositorio>

    criar uma branch local
        1 - git branch nome-da-branch
        2 - menu -> git -> new branch

    carregar os módulos de uma branch especifica                   [ git checkout <nome-da-branch> ]
    """

# Explicões extras
"git push origin master"  # pegar alterações, empurrar para o repositório remoto [ origin ], na branch [ master ]
"upstream"                # nome do repositório original

# Ações feitas na aula
"1"   # Foi feito 1 fork em aulas passadas, do repositório [ pythonpro / libpythonpro ] para [ renzon / libpythonpro ]
"2"   # Depois desse fork, foi feito uma clonagem, para poder usar o projeto numa IDE
"3"   # Mas, nessa aula o procedimento de clonagem repete-se, copiando o link SSH
"4"   # A intenção agora é clonar o repositório remotamente (eu achei confuso)
"5"   # COMANDO: git remote add apelido link SSH (CLONAR)
"6"   # COMANDO: git remote -v                   (LISTAR)
"7"   # COMANDO: git fetch -all                  (ATUALIZAR)
"8"   # Como resultado, uma nova BRANCH REMOTA surge, com o nome do apelido
"9"   # Depois, na BRANCH LOCAL, foi criado uma BRANCH NOVA pela opção [ + new branch ]
"10"  # Aparentemente, quando se faz isso, nada na tela é alterado, mas você está logado nessa BRANCH nova criada
"11"  # Após, é feito uma alteração qualquer no projeto, e então verifica-se [ menu -> git -> show git log ]
"12"  # Pela teoria, ações dessa BRANCH LOCAL criada, aparecem nesse log
"13"  # Voltando ao 10, acessando as BRANCHES novamente, é possível fazer migração entre as BRANCHES existentes
"14"  # Deslogando da BRANCH LOCAL: [ Menu -> git -> branches -> remote branches -> nome -> seta -> checkout ]
"15"  # A tela sofre uma alteração
"16"  # Depois é deletada a BRANCH LOCAL (essa opção talvez esteja disponível somente quando há + de 1 BRANCH LOCAL)
"17"  # Deletar BRANCH LOCAL [ Menu -> git -> branches -> local branches -> nome -> seta -> delete ]
"18"  # Pelo que foi entendido, repositórios remotos = BRANCH REMOTA
"19"  # Esses repositórios remotos, em trabalhos de equipe, normalmente recebem PULL REQUESTS
"20"  # Em 5 foi criado o repositório remoto, e agora ele irá tornar-se o local
"21"  # [ Git -> branches -> remote branches -> nome -> seta -> checkout as new local brench ]
"22"  # É executado um COMMIT/PUSH

"Título"  # Comando relacionados a branch pelas ferramentas da IDE (Pycharm) no projeto
def parte2():
    """
    [ Git / Manage Remotes... ]          # conectar um repositório remoto (Pycharm)
    [ Git / Fetch ]                      # atualizar todas as branches remotas de todos rep. remotos (Pycharm)
    [ Git / Branches... / + New branch ] # criar uma branch local (Pycharm)
    [ Git / Show Git Log ]               # verificar logs de braches feitas
    """