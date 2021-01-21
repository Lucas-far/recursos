

"""
Módulo: arquivo_gitignore.py
Palavra chave: gitignore global

Aula          || Arquivo Gitignore
Palavra_chave || tutorial gitignore
Objetivo      || criar um arquivo padrão para que nenhum dos conteúdos nele sejam integrados ao git
"""

# Configuração de um arquivo [ .gitignore ] global
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
