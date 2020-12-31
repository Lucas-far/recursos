

"""
Objetivo:
         listar objetos de bdd e mostrar seus dados de forma separada, em um novo template global
"""

def fonte():
    """ /home/lucas/PycharmProjects/objeto_rota_singular """

def terminal():
    """
    pip install django==2.2.17 django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['bootstrap4', 'pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """





# todo PARTE 1 - Configurar objetos com rota singular [ contexto = Function based view ]

def models():
    """
    from django.db import models
    from django.template.defaultfilters import slugify
    from django.db.models import signals

    class Modelofbv(models.Model):
        autor = models.CharField('Autor', max_length=200)
        texto = models.CharField('Texto', max_length=500)
        slug = models.SlugField('Slug', blank=True, editable=False, max_length=500)

        def __str__(self):
            return self.autor

        class Meta:
            verbose_name = 'fbv'
            verbose_name_plural = 'fbvs'

    def slugify_model_fbv(instance, **kwargs):
        instance.slug = slugify(instance.texto)
    signals.pre_save.connect(slugify_model_fbv, sender=Modelofbv)
    """

def admin():
    """
    from django.contrib import admin
    from .models import Modelofbv

    @admin.register(Modelofbv)
    class ModelofbvAdmin(admin.ModelAdmin):
        list_display = ('autor', 'texto',)
    """

def views():
    """
    from django.shortcuts import render
    from .models import Modelofbv

    def index(request):
        context = {'queryset': Modelofbv.objects.all()}
        return render(request, 'index.html', context)
    """

def pa_urls():
    """
    from django.urls import path
    from .views import index
    urlpatterns = [path('', index, name='index')]
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
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
        <title>Exibição de dados</title>
    </head>
    <body>
        {% for object in queryset %}
            <div><a href="#">{{ object.autor }}</a></div>
        {% endfor %}
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# Ir ao template admin Django e criar objetos, para poderem ser vistos no template

"======================================================================================================================"
# Até este momento, temos cada objeto, mas não temos seus dados apresentados singularmente
"======================================================================================================================"

def views2():
    """
    def object_single_path_fbv(request, slug):
        context = {'queryset': Modelofbv.objects.get(slug=slug)}
        return render(request, 'each-object-fbv.html', context)
    """

# Na rota, <tipo do campo:campo>
def pa_urls2():
    """
    from .views import object_single_path_fbv
    urlpatterns = [path('texto/<str:slug>', object_single_path_fbv, name='texto')]
    """

"index.html"  # modificação = adição da rota nova
def templates2():
    """ <div><a href="{% url 'texto' object.slug %}">{{ object.autor }}</a></div> """

"each_object_fbv.html"  # O template recebe o bdd gerado na view [ object_single_path_fbv ]
def templates3():
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
        <title>Exibição de dados</title>
    </head>
    <body>
        <table class="container table table-dark table-bordered">
            <thead>
                <tr>
                    <td>Autor</td>
                    <td>Texto</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{ queryset.autor }}</td>
                    <td>{{ queryset.texto }}</td>
                </tr>
            </tbody>
        </table>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """





# todo PARTE 2 - Configurar objetos com rota singular [ contexto = Class based view ]

def models2():
    """
    from django.db import models
    from django.template.defaultfilters import slugify
    from django.db.models import signals

    class Modelocbv(models.Model):
        autor = models.CharField('Autor', max_length=200)
        texto = models.CharField('Texto', max_length=500)
        slug = models.SlugField('Slug', blank=True, editable=False, max_length=500)

        def __str__(self):
            return self.autor

        class Meta:
            verbose_name = 'cbv'
            verbose_name_plural = 'cbvs'

    def slugify_model_cbv(instance, **kwargs):
        instance.slug = slugify(instance.texto)
    signals.pre_save.connect(slugify_model_cbv, sender=Modelocbv)
    """

def admin2():
    """
    from django.contrib import admin
    from .models import Modelocbv

    @admin.register(Modelocbv)
    class ModelocbvAdmin(admin.ModelAdmin):
        list_display = ('autor', 'texto',)
    """

def views3():
    """
    from django.views.generic import ListView
    from .models import Modelocbv

    class IndexListView(ListView):
        context_object_name = 'queryset'
        model = Modelocbv
        template_name = 'index2.html'
    """

def pa_urls3():
    """
    from .views import IndexListView
    urlpatterns = [path('index2/', IndexListView.as_view(), name='index2')]
    """

def templates4():
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
        <title>Exibição de dados</title>
    </head>
    <body>
        {% for object in queryset %}
            <div><a href="#">{{ object.autor }}</a></div>
        {% endfor %}
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def terminal3():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """

# Ir ao template admin Django e criar objetos, para poderem ser vistos no template

"======================================================================================================================"
# Até este momento, temos cada objeto, mas não temos seus dados apresentados singularmente
"======================================================================================================================"

def views4():
    """
    def object_single_path_cbv(request, slug):
        context = {'queryset': Modelocbv.objects.get(slug=slug)}
        return render(request, 'each-object-cbv.html', context)
    """

# Na rota, <tipo do campo:campo>
def pa_urls4():
    """
    from .views import object_single_path_cbv
    urlpatterns = [path('frase/<str:slug>', object_single_path_cbv, name='frase')]
    """

"index2.html"  # modificação = adição da rota nova
def templates5():
    """ <div><a href="{% url 'frase' object.slug %}">{{ object.autor }}</a></div> """

"each_object_cbv.html"  # O template recebe o bdd gerado na view [ object_single_path_cbv ]
def templates6():
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
        <title>Exibição de dados</title>
    </head>
    <body>
        <table class="container table table-dark table-bordered">
            <thead>
                <tr>
                    <td>Autor</td>
                    <td>Texto</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{ queryset.autor }}</td>
                    <td>{{ queryset.texto }}</td>
                </tr>
            </tbody>
        </table>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """
