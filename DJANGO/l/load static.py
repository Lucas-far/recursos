

# TODO -> Configurar {% load static %}

def terminal():
    """
    pip install django==2.2.9
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

# Variável Não mandatória, mas recomendável, pois módulos estáticos precisem de backup no modo: produção
"STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')"  # python manage.py collectstatic
def settings():
    """
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    STATIC_URL = '/static/'
    """

# IndexTemplateView / index.html
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

# Não existe, criar no pacote aplicação [pa]
def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('', IndexTemplateView.as_view(), name='index')]
    """

def pa_pastas():
    """
    pa/new/directory/templates    = criar módulo [ index.html ]
    pa/new/directory/static
    pa/static/new/directory/css   = criar módulo [ styles.css ]
    pa/static/new/directory/image = adicionar qualquer módulo de imagem
    pa/static/new/directory/js    = criar módulo [ scripts.js ]
    """

"Módulos estáticos"
def css():
    """ body {background-color: #222; color: white; font-family: gothic;} """

def image():
    """ bicicleta-caloi.jpg """

def js():
    """ function mensagem() {alert('Essa bicicleta é raiada...*3*\nmas é muito cara :(');} """

# index.html
def templates():
    """
    <!DOCTYPE html>
    {% load static %}
    <html lang="en">
    <head>
        <link href="{% static 'css/styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <title>Página Índice</title>
    </head>
    <body>
        <h2>Página Índice</h2>
        <hr>
        <img src="{% static 'image/bicicleta-caloi.jpg' %}">
        <div><button onclick="mensagem();">ver mensagem</button></div>
        <script src="{% static 'js/scripts.js' %}" type="text/javascript"></script>
    </body>
    </html>
    """

def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """
