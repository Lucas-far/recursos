

"""
Módulo: chaves_ssh.py

Aula          || Chaves SSH
Palavra_chave || gerar ssh
Objetivo      || Gerar chave ssh
"""

# Clonar um repositório (manualmente, sem auxílio de uma IDE)
def parte1():
    """
    1 - Um repositório pode ser clonado via link: [ https ] ou [ ssh ] em sua página no GitHub
    2 - Ir ao botão [ code (atualmente) ] e copiar o link SSH
    3 - No terminal

        EXEMPLO 1: git clone git@github.com:codingforentrepreneurs/eCommerce.git
        EXEMPLO 2: git clone git@github.com:codingforentrepreneurs/eCommerce.git one-ecommerce

        OBS: O primeiro exemplo foi clonado com o nome original do repositório
        OBS: O segundo exemplo foi clonado com um nome alternativo para o repositório
    """

# Comandos git para ambientes virtuais conectados a um repositório
def parte2():
    """
    1 - git init
    2 - git status
    3 - git add .
    4 - git commit -m 'Mensagem obtigatória'
    5 - git push
    """

# Criar no OS, sua chave SSH pessoal, para usar no GitHub
def parte3():
    """
    1 - [ Ubuntu  ] ssh-keygen -t rsa / [ Windows ] ssh-keygen.exe -t rsa
    2 - Digitar uma passphrase

       EXEMPLO: umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada

       OBS: Um diretório é criado em [ /home/seu_user/.ssh ]

    3 - Serão criados: [ public key ] + [ key fingerprint = SHA256 ] + [ key's randomart ]
    4 - Acessar seu avatar e clicar na opção [ Settings ] + [ SSH and GPG keys ] + [ New ssh key ]
    5 - Ir ao diretório [ /home/seu_user/.ssh ], procurar por [ cat id_rsa.pub ] e copiar o conteúdo

        PROCEDIMENTO VIA TERMINAL:
                                  1 - cd /home/seu_user/.ssh
                                  2 - cat id_rsa.pub
                                  3 - ctrl + c

    6 - Voltar ao GitHub, colar o conteúdo copiado no campo [ key ] e dar um título à sua chave no campo [ title ]
    7 - Salvar
    """
