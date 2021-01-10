

"""
Módulo >>> template_django_bootstrap.py

Objetivo:
         definir um template padrão configurado com o framework bootstrap, através do Django

Palavra chave >>> configurar django-bootstrap4
"""

def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="#" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <body>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """
