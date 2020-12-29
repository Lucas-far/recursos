

"""
Objetivo:
         template usado parar editar um objeto já criado, de um bdd
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

# Uma view de edição, é similar a uma view de criação, elas compartilham do mesmo template
def views():
    """
    from django.views.generic import UpdateView
    from django.urls import reverse_lazy
    from .models import Tasks
    from django.contrib.messages.views import SuccessMessageMixin

    class AlterTaskUpdateView(SuccessMessageMixin, UpdateView):
        fields = ('task',)
        model = Tasks
        success_message = 'Sua tarefa foi editada!'
        success_url = reverse_lazy('mytasks')
        template_name = 'create-task.html'
    """

# todo INÍCIO - configuração da rota customizada_______________________________________________________________________

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('editar/<int:pk>', AlterTaskUpdateView.as_view(), name='updatetask')]
    """

"tasks-table.html"  # <a class="btn btn-primary" href="{% url 'updatetask' task.pk %}">editar</a>
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

"create-task.html"  # essa view NÃO DEVE ter o atributo action="" na tag <form></form>
def templates3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/create-task-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Criar tarefa</title>
    </head>
    <body>
        {% include 'fixed-return-button.html' %}
        <div class="container">
            <div class="mb-5 mt-5 text-center text-secondary"><span class="span-title">Administrar tarefa</span><hr></div>
            <br>
            <p class="text-center text-warning">adicionar / editar</p>
            <form autocomplete="off" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <div class="row">
                    <div class="form-group ma">
                        <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma">
                            <!-- Campo de criação/edição -->
                            <label class="sr-only" for="task">Campo para reescrever/escrever uma nova tarefa</label>
                            <input type="text" class="form-control mb-2" id="task" name="task" placeholder="reescreva/escreva aqui sua tarefa" size="70">

                            <!-- Botão de criar -->
                            <div class="text-right">
                                <button class="btn btn-dark mt-3" form="this-form" type="submit">
                                    <a class="text-white">Salvar</a>
                                </button>
                            </div>

                            <!-- Botão de cancelar -->
                            <div class="text-right">
                                <a class="btn btn-danger mt-3" href="{% url 'mytasks' %}">Voltar</a>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"create-task-styles.css"
def css():
    """
    body {background-color: #171A21;}
    .btn-dark:hover a {text-decoration: none;}
    .ma {margin: auto;}
    .span-title {color: #ff4500; font-size: 3em;}
    /*span {animation: sideways alternate infinite 2s; font-size: 3em;}*/
    hr {background-color: #ff4500; height: 3px; box-shadow: 0 0 50px #ff4500; border-radius: 10px;}

    /*
    @keyframes sideways {
        0% {padding-left: 10px;}
        100% {padding-right: 10px;}
    }
    */
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """
