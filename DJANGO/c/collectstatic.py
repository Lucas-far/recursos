

# TODO -> Configurar python manage.py collecstatic

def terminal():
    """
    pip install django==2.2.9
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    TEMPLATES = [{'DIRS': ['templates']}]
    INSTALLED_APPS = ['pa']
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    """

def views():
    """
    from django.views.generic import TemplateView
    class IndexTemplateView(TemplateView):
        template_name = 'index.html'
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('', IndexTemplateView.as_view(), name='index')]
    """

"Primeiramente, insere-se apenas um módulo estático: 1 imagem"

# index.html
def templates():
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        {% load static %}
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <body>
        <h2>Página índice</h2>
        <hr>
        <div><img src="{% static 'image/jade.png' %}"></div>
        <script
            crossorigin="anonymous"
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        ></script>

        <script
            crossorigin="anonymous"
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        ></script>
    </body>
    </html>
    """

def terminal2():
    """
    python manage.py migrate
    python manage.py collectstatic
    python manage.py runserver
    """

"A imagem deve aparecer, mas quando muda-se para o modo produção [ DEBUG = False ], haverá problemas"
"Com [ DEBUG = False ], novos módulos estáticos não serão visíveis, caso sejam criados nesse modo, no Django"
# O que pode-se fazer?
"Retorna-se ao modo desenvolvimento"                       # DEBUG = True
"Adiciona-se um novo módulo estático"                      # <div><img src="{% static 'image/kitana.png' %}"></div>
"Verifica-se se o módulo estático foi, de fato, inserido"  # python manage.py runserver
"Se estiver tudo certo, coletam-se/atualizam-se os ME"     # python manage.py collectstatic
"Retorna-se ao modo produção"                              # DEBUG = False
"Verifica-se se o módulo estático renderiza"               # python manage.py runserver
