

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

""  # Foi feito 1 fork em aulas passadas, do repositório [ pythonpro / libpythonpro ] para [ renzon / libpythonpro ]
""  # Depois desse fork, foi feito uma clonagem, para poder usar o projeto numa IDE
""  # Mas, nessa aula o procedimento de clonagem repete-se, copiando o link SSH
""  # A intenção agora é clonar o repositório remotamente

"1"   # git remote add apelido link SSH (CLONAR)
"2"   # git remote -v                   (LISTAR)
"3"   # git fetch -all                  (ATUALIZAR)
"4"   # Os códigos criam um REMOTE BRANCH de apelido [ upstream ]

""  # [ menu -> git -> branches -> + new branch ] criação de um branch [ ramo ]
""  # Aparentemente, [ menu -> git -> branches -> + new branch ] é usada para criar BRANCH LOCAL apenas
""  # Ao criar o BRANCH LOCAL, a tela não muda, mas esse BRANCH loga no projeto, sobescrevendo o BRANCH LOCAL [ master ]
""  # Alteração em algo no projeto
""  # [ menu -> git -> show git log ] para verificar se a modificação é exibida no log

""  # No momento o BRANCH logado é [ ramo ]
""  # Migração entre BRANCHES existentes
""  # [ Menu -> git -> branches -> local branches -> master -> seta -> checkout ] para migrar ao BRANCH local [ master ]
""  # Diferente do logar em um BRANCH criado, o migrar causa alteração na tela
""  # [ Menu -> git -> branches -> local branches -> ramo -> seta -> checkout ] Ativando BRANCH LOCAL [ ramo ]
""  # [ Menu -> git -> branches -> local branches -> master -> seta -> delete ] Deletado BRANCH LOCAL [ master ]
""  # No momento há somente um BRANCH LOCAL [ ramo ]

""  # BRANCH REMOTOS, normalmente são criados em trabalhos de equipe, para recebem PULL REQUESTS
""  # Anteriormente, foi criado um BRANCH REMOTO [ upstream ], e este pode criar um novo BRANCH LOCAL
""  # [ Git -> branches -> remote branches -> upstream -> seta -> checkout as new local brench ] com nome [ master ]
""  # Nesse momento, volta-se a ter dois BRANCH LOCAIS [ ramo ] [ master = criado do BRANCH REMOTO = upstream ]
""  # COMMIT/PUSH (o painel de PUSH precisa ser modificado)
""  # No painel de PUSH, há um link, normalmente configurado ao nome do BRANCH LOCAL padrão [ master ]
""  # No painel de PUSH, modificar esse link para [ origin ]
""  # PUSH
""  # Segundo o instrutor, a intenção disso é sincronizar a BRANCH REMOTA com a LOCAL

"Resumo atual"  # BRANCH REMOTA [ upstream ] criou BRANCH LOCAL [ master ] + COMMIT/PUSH + link = origin + PUSH

""  # Não fica claro se os procedimentos anteriores são mandatórios para que o resto possa ser feito
""  # Tomando por base que "sim", agora, para cada nova alteração, cria-se um novo BRANCH LOCAL
""  # [ menu -> git -> branches -> + new branch ] que no contexto, recebe o nome [ 4 ]
""  # Mesma lógica citada anteriormente: ao criar um BRANCH LOCAL novo, este é ativado, sobescrevendo o antigo ativado
""  # Portanto, mudanças posteriores, acontecem nesse BRANCH LOCAL nomeado [ 4 ]
""  # Alteração em algo do projeto
""  # COMMIT/PUSH (mensagem do commit com a sintaxe close #4)

# todo -> Parada em 09:00

""  # No repositório matriz [ pythonpro / libpythonpro ], surge uma mensagem informando o BRANCH que recebeu PUSH
""  # Há um botão dropdown com um símbolo de BRANCH, que mostra os BRANCHES ativos (não foi alterado)
"29"  # [ Compare and pull request ] deve carregar a página, com o conteúdo do último COMMIT nela
"30"  # [ create pull request ] para validar o PULL REQUEST
"31"  # Caso o PULL REQUEST fosse negado, foram feitos os seguintes procedimentos

#  transcrição de uma mensagem não entendida com clareza
def mensagem2():
    """
    FALHA EM PULL REQUEST
    A ideia do feature branch é que a branch master, ela sempre fica sincronizada com o upstream para você não ter o
    trabalho de reverter código toda hora

    "32"  # [ Menu -> git -> branches -> local branches -> master -> seta -> checkout ]
    "33"  # [ Menu -> git -> branches -> local branches -> apelido -> seta -> delete ]

    SUCESSO EM PULL REQUEST
    1 - O código será integrado ao repositório original/matriz

    "34"  # [ Rebase and merge ] [ Confirm rebase and merge ]
    "35"  # [ Menu -> git -> branches -> local branches -> apelido -> seta -> delete -> delete tracked branch ]
    """

"36"  # [ git fetch apelido ] para atualizar ações ocorrentes na branch apelido/upstream
"37"  # [ menu -> git -> branches -> local branches -> apelido -> seta -> merge ] (Fundir branch upstream e master)
"38"  # COMMIT/PUSH
"39"  # Recomendação de efetuar sempre que possível [ git fetch ] para manter o código atualizado

"Título"  # Comando relacionados a branch pelas ferramentas da IDE (Pycharm) no projeto
def parte2():
    """
    [ Git / Manage Remotes... ]          # conectar um repositório remoto (Pycharm)
    [ Git / Fetch ]                      # atualizar todas as branches remotas de todos rep. remotos (Pycharm)
    [ Git / Branches... / + New branch ] # criar uma branch local (Pycharm)
    [ Git / Show Git Log ]               # verificar logs de braches feitas
    """