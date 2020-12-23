

""""""

# Configurações iniciais

def terminal():
    """
    pip install django django-bootstrap4 mysqlclient PyMySQL
    django-admin startproject pp .
    django-admin startapp pa
    pip freeze > requirements.txt
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = {'DIRS': ['templates']}

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dtb_attempt_api',
            'USER': 'luksadmin',
            'PASSWORD': 'passwort2772',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    """

def mysql_workbench():
    """ CREATE DATABASE dtb_attempt_api; """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """





# Botão fixo
"fixed_return_button.html"
def template_btn():
    """
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
            </div>
        </div>
    </div>
    """





# Passo 1
"Se não há um usuário logado, mostra-se anônimo, e fornece-se botões para criar ou logar conta"
"Se há, mostra-se o nome de usuário, e fornece-se botões relacionados à tarefas"
def views():
    """
    from django.contrib import messages
    from django.shortcuts import render

    def index(request):
        context = {}
        return render(request, 'index.html', context)
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('', index, name='index')]
    """

def template():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/index.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
    </head>
    <body>
        {% bootstrap_messages %}
        <div class="container mt-5 text-center">
            {% if request.user.is_anonymous == True %}
                <h2 class="text-secondary">Você está anônimo</h2>
                <p class="text-secondary">é preciso criar uma conta, para ter acesso ao site</p>
            {% else %}
                <h2 class="text-secondary">Seja bem-vindo, {{ request.user }}</h2>
                <div class="container">
                    <div class="row">
                        <div class="col-4 col-sm-4 col-md-4 col-lg-4 col-xl-4">
                            <a class="btn btn-success" href="#">Ver tarefas</a>
                        </div>
                        <div class="col-4 col-sm-4 col-md-4 col-lg-4 col-xl-4">
                            <a class="btn btn-primary" href="#">Adicionar tarefa</a>
                        </div>
                        <div class="col-4 col-sm-4 col-md-4 col-lg-4 col-xl-4">
                            <a class="btn btn-danger" href="#">Deletar tarefa</a>
                        </div>
                    </div>
                </div>
            {% endif %}
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css():
    """
    body {
        background-color: #222;
    }
    """

def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """





# Passo 2
"template para criar uma conta de usuário"
"os inputs [ atrib. name ] são baseados no nome dos campos do bdd User padrão do Django"
def views2():
    """
    from django.contrib.auth.models import User
    from django.shortcuts import redirect

    def sign_up(request):
        if str(request.method) == 'POST':
            if str(request.POST['password']) == str(request.POST['password_confirm']):
                if User.objects.filter(username=request.POST['username']).exists():
                    messages.error(request, 'O nome de usuário já existe.')
                elif User.objects.filter(email=request.POST['email']).exists():
                    messages.error(request, 'Já há uma conta registrada com esse e-mail.')
                else:
                    new_user = User.objects.create_user(
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password']
                    )
                    new_user.save()
                    messages.success(request, f'Cadastrado com sucesso, obrigado!. Seja bem-vindo, {new_user.get_full_name()}!')
                    return redirect('index')
            else:
                messages.error(request, 'Senha inicial e de confirmação, não são idênticas!')

        return render(request, 'sign-up-template.html')
    """

def pa_urls2():
    """
    urlpatterns = [path('sign_up/', sign_up, name='sign_up/']
    """

def template2():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet"> <!-- font-family: Itim -->
        <link href="{% static 'css/sign-up-styles' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Criar uma conta</title>
    </head>

    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
                </div>
            </div>
        </div>

        <main>
            <div class="container">
                <form action="{% url 'sign_up/' %}" autocomplete="off" id="this-form" method="post">
                    {% csrf_token %}
                    {% bootstrap_messages %}

                    <div class="row">
                        <div class="ma mt-5">
                            <h1 class="my-h1">Criação de conta</h1>
                            <hr>
                        </div>
                    </div>

                    <div class="row mt-5">
                        <div class="form-group ma mb-2">
                            <label class="sr-only" for="first_name">Campo para escrever o primeiro nome</label>
                            <input type="text" class="form-control" id="first_name" max="100" min="2" name="first_name" placeholder="seu primeiro nome" size="20" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="form-group ma mb-2">
                            <label class="sr-only" for="last_name">Campo para escrever o sobrenome</label>
                            <input type="text" class="form-control" id="last_name" max="100" min="2" name="last_name" placeholder="seu sobrenome" size="20"  required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="form-group ma mb-2">
                            <label class="sr-only" for="username">Campo para escrever o nome de usuário/apelido</label>
                            <input type="text" class="form-control" id="username" max="100" min="2" name="username" placeholder="seu nome de usuário" size="20" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="form-group ma mb-2">
                            <label class="sr-only" for="email">Campo para escrever e-mail</label>
                            <input type="email" class="form-control" id="email" max="100" min="2" name="email" placeholder="seu e-mail" size="20" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="form-group ma mb-2">
                            <label class="sr-only" for="password">Campo para escrever senha</label>
                            <input type="password" class="form-control" id="password" max="100" min="2" name="password" placeholder="sua senha" size="20" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="form-group ma mb-2">
                            <label class="sr-only" for="password_confirm">Campo para reescrever a senha</label>
                            <input type="password" class="form-control" id="password_confirm" max="100" min="2" name="password_confirm" placeholder="sua senha novamente" size="20" required>
                        </div>
                    </div>
                </form>
            </div>

            <div class="container">
                <div class="row">
                    <div class="ma mt-3">
                        <button class="btn btn-dark" type="submit" form="this-form">Registrar</button>
                    </div>
                </div>
            </div>
        </main>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css2():
    """
    body {background-color: #171A21; color: #c7d5e0;}
    .container-fluid {position: fixed; top: 0; background-color: #171A21;} /* cor de fundo deve ser = body */
    .btn-dark:hover a {text-decoration: none;}
    .ma {margin: auto;}
    .my-h1 {font-family: Itim;}
    hr {background-color: aqua; height: 3px; box-shadow: 0 0 50px aqua; border-radius: 10px;}
    .form-control {background-color: #171A21;}
    .form-control:focus {background-color: #171A21;}
    """





# Passo 3
"template para logar numa conta de usuário"
def views3():
    """
    from django.contrib.auth import authenticate, login

    def sign_in(request):
        if str(request.method) == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login efetuado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'O usuário ou a senha não existem!')
        return render(request, 'sign-in-template.html')
    """

def pa_urls3():
    """
    from .views import *

    urlpatterns = [path('sign_in/', sign_in, name='sign_in/')]
    """

def template3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/sign-in-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Efetuar login</title>
    </head>
    <body>

        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
                </div>
            </div>
        </div>

        <main>
            <div class="container">
                <form action="{% url 'sign_in/' %}" class="form" id="this-form" method="post">
                    <fieldset class="fieldset pb30px text-center">Login</fieldset>
                    {% csrf_token %}
                    {% bootstrap_messages %}

                    <div class="row">
                        <div class="form-group ma">
                            <label class="blink-text" for="username">Nome de usuário</label>
                            <label class="sr-only" for="username">Campo para escrever o nome de usuário/apelido</label>
                            <input class="form-control" id="username" max="100" min="2" name="username" type="text" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="form-group ma mb-5">
                            <label class="blink-text"  for="password">Senha</label>
                            <label class="sr-only" for="password">Campo para escrever senha</label>
                            <input class="form-control" id="password" max="100" min="2" name="password" type="password" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="ma">
                            <button class="btn btn-dark" form="this-form" type="submit">Logar</button>
                        </div>
                    </div>
                </form>
            </div>
        </main>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css3():
    """
    body {background-color: #171A21; color: #0e3742;}
    .container-fluid {position: fixed; top: 0; background-color: #171A21;} /* cor de fundo deve ser = body */
    .btn-dark:hover a {text-decoration: none;}
    main {margin-top: 100px;}  /* espaçamento necessário para evitar que o conteúdo seja sobreposto pelo botão fixo */
    .fieldset {
        font-size: 7em;
        color: #fff;
        text-shadow: 0 1px 10px #1b2838,
                     0 2px 20px #2a475e,
                     0 3px 0 #1b2838,
                     0 4px 0 #2a475e,
                     0 5px 0 #1b2838,
                     0 6px 0 #2a475e,
                     0 7px 0 #1b2838,
                     0 8px 0 #2a475e,
                     0 9px 0 #1b2838,
                     0 10px 0 #2a475e;
    }
    .blink-text {animation: blink-text linear infinite 15s;}
    .form-control {background-color: #171A21;}
    .form-control:focus {background-color: #171A21;}
    .ma {margin: auto;}

    @keyframes blink-text {
        0%,18%,20%,50.1%,60%,65.1%,80%,90.1%,92% {
            color: #fff; text-shadow: none;
        }
        18.1%,20.1%,30%,50%,60.1%,65%,80.1%,90%,92.1%,100% {
            color: #171A21;
            text-shadow: 0 0 5px #03bcf4,
                         0 0 6px #03bcf4,
                         0 0 7px #03bcf4,
                         0 0 8px #03bcf4,
                         0 0 9px #03bcf4;
        }
    }
    """





# Passo 4
"é preciso adicionar os botões de criar conta e login"
"inserir dentro do {% if %}{% endif %}, pois o usuário: não existe ou não está logado"
def template4():
    """
    <a class="btn btn-primary" href="{% url 'sign_up/' %}">Criar conta</a>
    <a class="btn btn-success" href="{% url 'sign_in/' %}">Login</a>
    """





# Passo 5
"é preciso que o usuário possa deslogar, caso deseje"  # Fonte: https://www.youtube.com/watch?v=tUqUdu0Sjyc -> 29:33
def views4():
    """
    from django.contrib.auth import logout

    def sign_out(request):
        messages.success(request, 'Saída efetuada com sucesso')
        logout(request)
        return redirect('index')
    """

def pa_urls4():
    """ urlpatterns = [path('sign_out/', sign_out, name='sign_out/] """

# index.html, botão inserido no {% else %}, pois o usuário já está logado
def template5():
    """
    <a class="btn btn-dark text-danger mb-3" href="{% url 'sign_out/' %}">Deslogar</a>
    """





# Passo 6
"é preciso criar o bdd para armazenar tarefas adicionadas"
def models():
    """
    class Base(models.Model):
        created = models.DateTimeField('Data de criação', auto_now_add=True)
        updated = models.DateTimeField('Última atualização', auto_now=True)

    class Tasks(Base):
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

def terminal3():
    """
    python manage.py makemigrations
    python manage.py migrate
    """





# Passo 7
"construir a lógica do botão de ver tarefas"
def views5():
    """
    from django.views.generic import ListView
    from .models import Tasks

    class TasksListView(ListView):
        context_object_name = 'queryset'  # .objects.all() [ para loop for ]
        model = Tasks
        ordering = 'created'              # por qual campo começar a mostrar dados
        paginate_by = 5                   # ativar lógica de paginação (se há), a partir do valor
        template_name = 'my-tasks.html'
    """

def pa_urls5():
    """
    urlpatterns = [path('my-tasks/', TasksListView.as_view(), name='my-tasks/')]
    """

"pagination.html"
def template6():
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

"index.html"
def template7():
    """
    <div class="col-4 col-sm-4 col-md-4 col-lg-4 col-xl-4">
        <a class="btn btn-success" href="{% url 'my-tasks/' %}">Ver tarefas</a>
    </div>
    """

"my-tasks.html"
def template8():
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
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
                </div>
            </div>
        </div>
        <div class="container">
            <h2 class="mb-5 mt-5 text-primary">Suas tarefas</h2>
            <table class="table table-dark table-bordered">
                <thead>
                    <tr>
                        <th class="bg-secondary">Tarefa</th>
                        <th class="bg-info">Data de adição</th>
                        <th class="bg-warning">Ações</th>
                    </tr>
                </thead>

                <tbody>
                {% for tasks in queryset %}
                    <tr>
                        <td class="bg-success">{{ tasks.task }}</td>
                        <td>{{ tasks.created }}</td>
                        <td class="text-center">
                            <a class="btn btn-primary" href="#">editar</a>
                            <a class="btn btn-danger" href="#">deletar</a>
                        </td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
            {% include 'pagination.html' %}
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css4():
    """
    body {background-color: #292929;}
    """





# Passo 8
"constuir a lógica do botão de criar tarefa"
def views6():
    """
    from django.contrib.messages.views import SuccessMessageMixin
    from django.urls import reverse_lazy
    from django.views.generic import CreateView

    class NewTaskCreateView(SuccessMessageMixin, CreateView):
        fields = ('task',)
        model = Tasks
        success_url = reverse_lazy('my-tasks/')
        template_name = 'create-task.html'
        success_message = 'Uma nova tarefa foi adicionada!'
    """

def pa_urls6():
    """
    urlpatterns = [path('create-task/', NewTaskCreateView.as_view(), name='create-task/')]
    """

def template9():
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
            <div class="mb-5 mt-5 text-center text-secondary"><span>Tarefa nova</span><hr></div>
            <form action="{% url 'create-task/' %}" autocomplete="off" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <div class="row">
                    <div class="form-group ma">
                        <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma">
                            <!-- Campo de criação -->
                            <label class="sr-only" for="task">Campo para escrever uma nova tarefa</label>
                            <input type="text" class="form-control mb-2" id="task" name="task" placeholder="escreva aqui sua tarefa nova" size="70">

                            <!-- Botão de criar -->
                            <button class="btn btn-dark mt-3" form="this-form" type="submit">
                                <a class="text-white">Salvar</a>
                            </button>

                            <!-- Botão de cancelar -->
                            <a class="btn btn-danger mt-3 text-white" href="{% url 'my-tasks/' %}">Voltar</a>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css5():
    """
    body {background-color: #171A21;}
    .btn-dark:hover a {text-decoration: none;}
    .ma {margin: auto;}
    span {animation: sideways alternate infinite 2s; font-size: 3em;}
    hr {background-color: aqua; height: 3px; box-shadow: 0 0 50px aqua; border-radius: 10px;}

    @keyframes sideways {
        0% {padding-left: 10px;}
        100% {padding-right: 10px;}
    }
    """
