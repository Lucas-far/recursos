

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





# View: index
def views():
    """
    from django.shortcuts import render

    def index(request):
        context = {}
        return render(request, 'index.html', context)
    """

# Rota da view: index
def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('', index, name='index')]
    """

# Template: index.html
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
                <a class="btn btn-primary" href="{% url 'criar-conta/' %}">Criar sua conta</a>
            {% else %}
                <h2 class="text-secondary">Seja bem-vindo, {{ request.user }}</h2>
            {% endif %}
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# Css: index.css
def css():
    """
    body {
        background-color: #222;
    }
    """

# Testar se as configurações iniciais estão corretas
def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """





# View: sign_up
def views2():
    """
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

        return render(request, 'criar-conta.html')
    """

# Rota da view: criar-conta/
def pa_urls2():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('criar-conta/', sign_up, name='criar-conta/']
    """

# Template: criar-conta.html
def template2():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet"> <!-- font-family: Itim -->
        <link href="{% static 'css/criar-conta.css' %}" rel="stylesheet">
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
                <form action="{% url 'criar-conta/' %}" autocomplete="off" id="this-form" method="post">
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

# Css: criar-conta.css
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
