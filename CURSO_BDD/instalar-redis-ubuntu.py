

"""
Módulo >>> instalar-redis-ubuntu.py

Objetivo:
         configurar o bdd noSQL Redis no OS Ubuntu
"""

def fonte():
    """
    Curso  # Bancos de Dados SQL e NoSQL do básico ao avançado
    Seção  # Seção 13:Redis - Parte 1
    Aula   # 139. Instalação e Configuração no Linux
    """

"2"  # Pacote de compiladores em C, C++, bibliotecas de compartilhamento
def terminal():
    """
    1 - sudo apt-get update
    2 - sudo apt-get install build-essential -y
    """

"Download"  # https://redis.io/ >>> Downloads / Stable version / Download

# Procedimentos recomendáveis no OS
def os():
    """
    1 - Ir ao diretório de downloads
    2 - Botão direito no instalador do Redis, e [ extract here ]
    3 - Renomear diretório para [ Redis ]
    4 - Se não há, vá a rota [ /home/seu_user ] e crie um diretório [ apps ], ficando: [ /home/seu_user/apps ]
    5 - Mover o diretório do Redis para a rota especificada em 4
    """

"Redis"  # Instalação da versão console
# Procedimentos a serem feitos no diretório do Redis
def os2():
    """
    1. Entrar no diretório [ Redis ]
    2. Em qualquer área vazia, clique [ botão direito / open in terminal ]
    3. No terminal, digitar [ make ]
    4. Um procedimento de compilação ocorrerá (não é rápido)
    5. No terminal, digitar [ make test ]
    6. No terminal, digitar [ sudo apt-get install tcl 8.5 -y ] (muito demorado)
    7. No terminal, digitar [ make test ]
    8. Dentro do diretório [ redis ], há o diretório [ src ]. Abra-o.
    9. Procurar pelos módulos [ redis-cli ] & [ redis-server ]
    10. No diretório [ redis/src ] clique em algum espaço vazio [ botão direito / open in terminal ]
    11. No terminal, digitar [ cd /usr/local/bin/ ]
    12. No terminal, digitar [ sudo ln -s /home/lucas/apps/redis/src/redis-cli . ] para criar um link simbólico
    13. No terminal, digitar [ sudo ln -s /home/lucas/apps/redis/src/redis-server . ] para criar um link simbólico
    14. Feche o terminal
    15. Abra o terminal
    16. No terminal, digitar [ redis-cli --version ]
    17. No terminal, digitar [ redis-server --version ]
    """

"Redis"  # Instalação da interface gráfica
def browser2():
    """
    https://www.electronjs.org/apps/p3x-redis-ui   ||   p3x redis ui / redis ui

    1. Na lateral esquerda da tela do website, clique no link onde está a palavra [ repository  ]
    2. O link do repository é [ github.com/patrikx3/redis-ui ], adicione [ /releases ] ao link
    3. Aparentemente, deve-se escolher a opção [ P3X-Redis-UI-2020.10.499.AppImage ]
    4. Faça o download dessa opção
    """

# Procedimentos a serem feitos com a interface gráfica
def ubuntu_dir_downloads():
    """
    1 - Mover o executável do diretório de [ Downloads ] para o diretório [ /home/seu_user/apps ]
    2 - Entrar no diretório do software movido para [ /home/seu_user/apps ]
    3 - Em uma área vazia da tela: [ botão direito / Open in Terminal ]
    """

# Converter o módulo para este tornar-se um executável e então instalar
def terminal2():
    """
    1 - chmod +x P3X-Redis-UI-2020.10.499.AppImage
    2 - ./P3X-Redis-UI-2020.10.499.AppImage
    3 - Após 2, será aberto a interface do bdd [ Redis ]
    4 - Após a instalação da interface gráfica, ela pode ser acessada em [ Show applications ]
    """

# Ativar o servidor que faz o Redis funcionar
def terminal3():
    """
    1 - Ir ao diretório do [ /home/seu_user/redis/ src ]
    2 - Em uma área vazia da tela, fazer: [ botão direito / Open in Terminal ]
    3 - ./redis-server ]
    """
