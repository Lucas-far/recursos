

"""
Módulo >>> sign-up.py

Objetivo:
         criar um template que execute a criação de um objeto de usuário

Criar uma conta:
                /home/lucas/PycharmProjects/attempt_api
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

# Lógica usando o bdd padrão do Django [ User ]
def views():
    """
    from django.shortcuts import render
    from django.contrib import messages
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

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [path('signup', sign_up, name='signup')]
    """

"fixed-return-button.html"  # Template contendo um botão fixo para usar em templates de forma geral
def templates():
    """
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
            </div>
        </div>
    </div>
    """

"sign-up-form.html"  # Template contendo somente os campos, inserido em sintaxe {% include 'nome_template.html' %}
def templates2():
    """
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
    """

"sign-up.html"  # Template principal, contendo a tag do formulário, que receberá o template com os campos
def templates3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/sign-up-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Efetuar login</title>
    </head>

    <body>
        {% include 'fixed-return-button.html' %}
        <main class="mt-5">
            <div class="container mt-5 text-center">
                <h1 class="my-h1 ">Criar sua conta</h1>
                <hr>
            </div>
            <div class="container">
                <form action="{% url 'signup' %}" class="form" id="this-form" method="post">
                    {% csrf_token %}
                    {% bootstrap_messages %}
                    {% include 'sign-up-form.html' %}
                    <div class="row">
                        <div class="ma">
                            <button class="btn btn-dark" form="this-form" type="submit">Registrar</button>
                        </div>
                    </div>
                </form>
            </div>
        </main>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"sign-up-styles.css"
def css():
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
