

"""
Objetivo:
         carregar o console shell django

Comando:
        python manage.py shell
"""

# Exemplos de importação
def importar():
    """
    IMPORTAÇÃO DE MÓDULOS
        from pp.settings import *
        DATABASES

    IMPORTAÇÃO DE BIBLIOTECAS
        from django.urls import path
        dir(path)
    """

# Manipulação de objetos de bdd
def objetos():
    """
    ITERAÇÃO GLOBAL

        python manage.py shell
        from pa.models import Modelo
        var = Modelo.objects.all()

        for obj in var:
            print(obj)

    ITERAÇÃO ESPECÍFICA

        python manage.py shell
        from pa.models import Modelo
        var = Modelo.objects.all()

        for obj in var:
            print(obj.name, obj.price, obj.storage)
    """
