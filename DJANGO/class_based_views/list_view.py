

"""
Módulo: list_view.py

Objetivo:
         template usado parar exibir dados de bdd, seja ou não, em forma de tabela

Palavra chave:
              configurar list view
"""

# Configurações iniciais
def terminal():
    """
    pip install django django-bootstrap4
    django-admin startproject pp .
    django-admin startapp pa
    pip freeze > requirements.txt
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = {'DIRS': ['templates']}
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def models():
    """
    from django.db import models

    class Tasks(models.Model):
        task = models.CharField('Qual a tarefa a ser adicionada?', max_length=1500)

        def __str__(self):
            return self.task

        class Meta:
            verbose_name = 'Tarefa'
            verbose_name_plural = 'Tarefas'
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Tasks)
    class TasksAdmin(admin.ModelAdmin):
        list_display = ('task',)
    """

"context_object_name"   # nome da var para o loop for: {% for var_interna in var %} / Modelo.objects.all()
"model"                 # modelo criado que será chamado no template
"ordering"              # se há paginação, essa var ordenada os dados pelo campo especificado como valor
"paginate_by"           # se há paginação, o valor dessa var define a partir de quantos objetos cria-se a próxima página
"template_name"         # var para informar o nome do template onde o bdd será renderizado
"def get_context_data"  # quando quer-se restringer o usuário de ver/executar tarefas, caso não esteja logado
def views():
    """
    from django.views.generic import ListView
    from .models import Tasks

    class TasksListView(ListView):
        context_object_name = 'queryset'
        model = Tasks
        ordering = 'created'
        paginate_by = 5
        template_name = 'my-tasks.html'

        def get_context_data(self, **kwargs):
            context = super(TasksListView, self).get_context_data(**kwargs)
            context['database'] = Tasks.objects.all()
            return context
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('mytasks', TasksListView.as_view(), name='mytasks')]
    """

"task-table.html"             # um exemplo de tabela que contenha um bdd
"{% for task in queryset %}"  # queryset = context_object_name
def templates():
    """
    <table class="table table-dark table-bordered">
        <thead>
            <tr>
                <th class="bg-secondary">Tarefa</th>
                <th class="bg-info">Data de adição</th>
                <th class="bg-warning">Ações</th>
            </tr>
        </thead>

        <tbody>
        {% for task in queryset %}
            <tr>
                <td class="bg-success">{{ task.task }}</td>
                <td>{{ task.created }}</td>
                <td class="text-center">
                    <a class="btn btn-primary" href="{% url 'updatetask' task.pk %}">editar</a>
                    <a class="btn btn-danger" href="{% url 'deletetask' task.pk %}">deletar</a>
                </td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
    """

"pagination.html"
def templates2():
    """
    {% if is_paginated %}
        <nav aria-label="nav-page">
            <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
            {% endif %}

            {% for each_page in paginator.page_range %}
                {% if page_obj.number == each_page %}
                    <li class="page-item active"><a class="page-link" href="#">{{ each_page }}</a></li>
                {% else %}
                    <li class="page-item"><a class="page-link" href="?page={{ each_page }}">{{ each_page }}</a></li>
                {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li>
            {% endif %}
            </ul>
        </nav>
    {% endif %}
    """

def templates3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/my-tasks-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Tarefas - ListView</title>
    </head>
    <body>
        {% bootstrap_messages %}
        {% include 'fixed-return-button.html' %}
        {% if database|length == 0 %}
            <div class="container mt-5 text-center">
                <h2 class="text-danger">Não há tarefas adicionadas!</h2>
                <hr>
                <a class="btn btn-primary" href="{% url 'createtask' %}">Adicionar tarefa</a>
            </div>
        {% else %}
            <div class="container">
                <h2 class="mb-5 mt-5 text-primary">Suas tarefas</h2>
                {% include 'tasks-table.html' %}
                {% include 'pagination.html' %}
            </div>
        {% endif %}
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"my-tasks-styles.css"
def css():
    """
    body {background-color: #292929;}
    hr {background-color: #d32323; height: 3px; box-shadow: 0 0 50px #d32323; border-radius: 10px;}
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """
