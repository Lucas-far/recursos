

"""

"""

# -> Criação de Repositório
def setor_1_aula_2():
    """
    1 - criação de um repositório remoto pelo Github com nome: [ libpythonpro ]
    2 - nomemclatura [ pythoprobr / libpythonpro ] -> [ organização / nome do repositório remoto na conta github ]
    """

# -> Chaves SSH
def setor_1_aula_3():
    """
    1 - Acessar arquivo [ chaves_ssh.py ]
    2 - É mostrado a página de um repositório remoto [ github.com/requests/requests ]
    3 - O professor clona o repositório pelo botão [ code ] usando [ SSH ]
    4 - O GIT BASH do Windows é aberto

    OBS:
        - Os comandos abaixo, só funcionam com o Git instalado

    5 - git clone https://github.com/requests/requests.git nome_pasta

    OBS:
        - nome_pasta = nome do repositório, podendo ser qualquer coisa
        - nome_pasta = se deixado em branco, é usado o nome do próprio repositório remoto clonado

    6 - cd nome_pasta
    7 - git push origin master

    OBS:
        - o procedimento não dá certo, pois o usuário do professor não possui permissão
    """

# -> Fork
def setor_1_aula_4():
    """
    1  - O repositório remoto alvo ainda é [ github.com/requests/requests ]
    2  - Dessa vez, ao invés de tentar clonar, o professor usa o botão [ fork ] para sua conta [ renzon / requests ]
    3  - Ele vai ao seu repositório e usa o botão [ code ] para clonar via [ SSH ]
    4  - git clone https://github.com/renzon/requests.git
    5  - O repositório local do projeto é criado via Pycharm [ IDE do professor ]
    6  - Uma alteração é feita
    7  - git add .
    8  - git commit -m 'msg'
    9  - O professor retorna à página do repositório remoto
    10 - A aba [ pull requests ] é clicada
    11 - O botão [ New pull request ] é acionado
    12 - O botão [ Create pull request ] é acionado
    """

# -> Pull Request
def setor_1_aula_5():
    """
    1  - Repositório remoto [ https://github.com/pythonprobr/libpythonpro ]
    2  - Repositório remoto recebe [ fork ]
    3  - Repositório remoto com fork [ https://github.com/renzon/libpythonpro ]
    4  - Repositório clonado via chave SSH
    5  - git clone git@github.com:renzon/libpythonpro.git
    6  - alteração em um dos arquivos do projeto
    7  - git commit -am 'msg'
    8  - na página mencionada no item 3, o link [ commit ] será incrementado
    9  - o botão [ new pull request ] torna-se disponível e é acionado
    10 - o botão [ create pull request ] é acionado para abrir a sessão e enviar (botões iguais, funções diferentes)
    11 - o [ pull request ], é criado no [ item 3 ], para ser enviado ao [ item 1 ]
    12 - A partir desse momento, um colaborador verificaria seu pull request
    13 - No caso do pull request ser aceito, o botão [ merge pull request ] é acionado
    13 - Mas este botão possui opções, e o professor escolheu [ rebase and merge ]
    """

# -> Pull Request Não Aceito
def setor_1_aula_6():
    """
    1  - Repositório remoto [ https://github.com/pythonprobr/libpythonpro/ ]
    2  - É acessada a aba [ issues ] e acionado o botão [ new issue ]
    3  - Ao fazer isso, torna-se disponível uma postagem, com [ título ] e [ área de postagem ]
    4  - Ao finalizar, acionar o botão [ submit new issue ]
    5  - Cada [ issue ] criada, gera uma hash [ EX: #4 ]
    6  - Retorna-se ao repositório local [ libpythonpro ]
    7  - alteração de algum arquivo (uso da linguagem markdown) [título substituidor do link] (link puro)
    8  - git commit -am 'msg'
    9  - Na mensagem do commit, o professor adiciona a hash da issue, junto com uma palavra comando [ close #4 ]
    10 - git push
    11 - Repositório remoto com fork [ https://github.com/renzon/libpythonpro/ ]
    12 - Acionar o botão [ new pull request ]
    13 - Acionar o botão [ create pull request ] (botão de criação)
    14 - Na [ área de postagem ], se for digitado [ close #4 ], uma referência ao seu issue será exibida
    15 - Acionar o botão [ create pull request ] (botão de envio)
    16 - Caso não aceito, foi recomendado o comando [ git reser --hard HEAD^1 ] (não recomendado)
    """

# -> Feature Branch
def setor_1_aula7():
    """
    1  - Repositório local [ libpythonpro ]

    OBS: Como este repositório é resultado de um [ fork ], seguido de um [ clone ], ele possui um branch remoto
    OBS: branch local: master
    OBS: branch remoto: origin/master

    2 - git remote -v -------------------------------------------------------------> listar branches remotos existentes

    OBS: Segundo o professor, o repositório local aponta somente para o repositório remoto com fork
    OBS: Segundo o professor, o repositório remoto original precisa ser chamado para o repositório local, também
    OBS: O nome padrão do repositório remoto original, chama-se [ upstream ]

    3 - Ir ao repositório remoto original [ https://github.com/pythonprobr/libpythonpro ]
    4 - [ ctrl + c ] link SSH
    5 - Retorna-se ao repositório local [ libpythonpro ]
    6 - git remote add upstream git@github.com:pythonprobr/libpythonpro.git
    7 - git fetch --all --------------------------------------------------------------------> atualizar mudanças feitas
                        * ao fazer isso, o branch remoto [ upstream ] será exibido como novo branch remoto
    8 - git checkout -B ramo --------------------------------------------------------------> criação de um branch local
                             * lembrando que, um branch local novo, contêm os arquivos do branch local anterior a ele
                             * se no contexto dessa aula, havia apenas um branch local [ master ]
                             * então o novo branch local [ ramo ] possui tudo que o anterior têm
    9 - alteração de algum arquivo
    10 - git commit -am 'msg'
    11 - git checkout master ------------------------------------------------------> retorno ao branch local [ master ]
                             * o retorno foi feito para mostrar que esta não foi afetada pelas mudanças
    12 - git checkout ramo ----------------------------------------------------------> retorno ao branch local [ ramo ]
    13 - git branch -D master -------------------> deletar o branch local [ master ] de dentro do branch local [ ramo ]
                              * não é possível deletar um branch local alvo, estando dentro deste

    OBS: O professor insere um contexto
    OBS: O professor explica que o branch remoto [ upstream ] receberá PULL REQUEST de outros desenvolvedores

    14 - O branch local ativado neste momento da aula: [ ramo ]
    15 - git checkout -B master upstream/master ---------------> criação de um branch local através de um branch remoto
                                                * master          = nome do branch local que será criado
                                                * upstream/master = nome do branch remoto, que criou o local

    OBS: Atualmente, o branch local ativado é: [ master ] vindo do branch remoto [ upstream/master ]
    OBS: O professor, nesse momento da aula, quer realizar um [ git push ]
    OBS: Antes de mais nada, vejamos todos os branches disponíveis pelo [ git branch --all ]

      [A] - * master
      [B] -   ramo
      [C] -   remotes/origin/HEAD -> origin/master
      [D] -   remotes/origin/master
      [E] -   remotes/upstream/dependabot/pip/src/django-1.11.29
      [F] -   remotes/upstream/master

    OBS: Se eu não entendi errado, ele quer sincronizar [A], que está ligado diretamente ao [F], com [D]

    16 - git push origin upstream/master --------------------> uma aparente sincronização, que não ficou claro para mim
                                         * origin          = item [D]
                                         * upstream/master = item [A] chamado indiretamente pelo seu criador: item [F]
    """
