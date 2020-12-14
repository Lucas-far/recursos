

# TODO -> Configurar {% load i18n %}

def terminal():
    """
    pip install django==2.2.9
    pip install django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

# IndexTemplateView / index.html
def views():
    """
    from django.views.generic import TemplateView

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'
    """

# OtherTemplateView / other.html
def views2():
    """
    from django.views.generic import TemplateView

    class OtherTemplateView(TemplateView):
        template_name = 'other.html'
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
    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index')
        path('other/', OtherTemplateView.as_view(), name='other/')
    ]
    """

"OBS: Dois templates idênticos, porém, [ index.html ] está com bootstrap4 configurado no template"

# index.html
def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <div class="container-fluid mt-5 text-center">
            <div class="border border-dark rounded-pill mb-5">
                <h2 class="text-dark">div class="border border-dark<br>h2 class="text-dark</h2>
            </div>
            <a class="btn btn-dark text-danger">class="btn btn-dark text-danger</a>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# other.html
def templates2():
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <div class="container-fluid mt-5 text-center">
            <div class="border border-dark rounded-pill mb-5">
                <h2 class="text-dark">div class="border border-dark<br>h2 class="text-dark</h2>
            </div>
            <a class="btn btn-dark text-danger">class="btn btn-dark text-danger</a>
        </div>
    </body>
    </html>
    """

def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """
