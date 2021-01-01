

"""
Módulo >>> shell.py

Objetivo:
         carregar o console shell django, e mostrar possíveis usos do recurso

Comando:
        python manage.py shell
"""

# Exemplos de importação módular
def terminal_shell():
    """
    python manage.py shell
    from pp.settings import *
    DATABASES
    INSTALLED_APPS
    MIDDLEWARE
    ...
    """

# Exemplo de importação de biblioteca
def terminal_shell2():
    """
    python manage.py shell
    from django.urls import path
    from django.db import models
    from django.
    dir(path)
    dir(models)
    """

# Exemplo de manipulação de objetos de bdd
def objetos():
    """
    python manage.py shell
    from pa.models import Modelo
    var = Modelo.objects.all()

    for obj in var:
        print(obj)

    for obj in var:
        print(obj.name, obj.price, obj.storage)
    """
