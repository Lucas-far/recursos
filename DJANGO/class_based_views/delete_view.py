

"""
Módulo: delete_view.py

Objetivo:
         template usado parar deletar um objeto já criado, de um bdd
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

# Diferente da view de criação e edição, uma view de deletamento precisa ser criada separadamente
def views():
    """
    from django.views.generic import DeleteView
    from django.urls import reverse_lazy
    from .models import Tasks
    from django.contrib.messages.views import SuccessMessageMixin

    class EraseTaskDeleteView(SuccessMessageMixin, DeleteView):
        model = Tasks
        success_message = 'Sua tarefa foi editada!'
        success_url = reverse_lazy('mytasks')
        template_name = 'delete-task.html'
    """

# todo INÍCIO - configuração da rota customizada_______________________________________________________________________

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('deletar/<int:pk>', EraseTaskDeleteView.as_view(), name='deletetask')]
    """

"tasks-table.html"  # <a class="btn btn-danger" href="{% url 'deletetask' task.pk %}">deletar</a>
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

# todo FIM - configuração da rota customizada__________________________________________________________________________

"fixed-return-button.html"  # Template contendo um botão fixo para usar em templates de forma geral
def templates2():
    """
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
            </div>
        </div>
    </div>
    """

"delete-task.html"  # essa view NÃO DEVE ter o atributo action="" na tag <form></form>
def templates3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/delete-task-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <body>
        {% bootstrap_messages %}
        <form autocomplete="off" method="post">
            {% csrf_token %}
            <div class="container mt-5 text-center">
                <span class="this-span text-danger">Deletar</span>
                <hr>
                <p class="mt-5 text-danger">Você deseja deletar a tarefa em destaque?</p>
                <p class="text-primary">{{ object }}</p>
                <button class="btn btn-danger" type="submit">sim, delete!</button>
                <a class="btn btn-primary" href="{% url 'mytasks' %}">não, voltar!</a>
            </div>
        </form>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"delete-task-styles.css"
def css():
    """
    body {background-color: #171A21;}
    .this-span {font-size: 2.7em;}
    hr {background-color: #d32323; height: 3px; box-shadow: 0 0 50px #d32323; border-radius: 10px;}
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """
