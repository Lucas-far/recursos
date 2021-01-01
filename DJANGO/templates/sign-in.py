

"""
Módulo >>> sign-in.py

Objetivo:
         criar um template que execute a entrada de uma conta já criada

Exemplo:
        /home/lucas/PycharmProjects/attempt_api
"""

def terminal():
    """
    pip install django==2.2.17 django-bootstrap4
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

# Lógica de autenticação
def views():
    """
    from django.shortcuts import render
    from django.contrib import messages
    from django.contrib.auth import authenticate, login, logout
    from django.shortcuts import redirect

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

# Lógica da saída
def views2():
    """
    def sign_out(request):
        messages.success(request, 'Saída efetuada com sucesso')
        logout(request)
        return redirect('index')
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [path('signin', sign_in, name='signin')]
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

"sign-in-form.html"  # Template contendo somente os campos, inserido em sintaxe {% include 'nome_template.html' %}
def templates2():
    """
    <div class="row">
        <div class="form-group ma mb-2">
            <label class="blink-text" for="username">Nome de usuário</label>
            <label class="sr-only" for="username">Campo para escrever o nome de usuário/apelido</label>
            <input class="form-control" id="username" max="100" min="2" name="username" type="text" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-3">
            <label class="blink-text"  for="password">Senha</label>
            <label class="sr-only" for="password">Campo para escrever senha</label>
            <input class="form-control" id="password" max="100" min="2" name="password" type="password" required>
        </div>
    </div>
    """

"sign-in.html"  # Template principal, contendo a tag do formulário, que receberá o template com os campos
def templates3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet"> <!-- font-family: Itim -->
        <link href="{% static 'css/sign-in-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Criar uma conta</title>
    </head>

    <body>
        {% include 'fixed-return-button.html' %}
        <main>
            <div class="container">
                <form action="{% url 'signin' %}" autocomplete="off" id="this-form" method="post">
                    <fieldset class="fieldset pb30px text-center">Login</fieldset>
                    {% csrf_token %}
                    {% bootstrap_messages %}
                    {% include 'sign-in-form.html' %}
                </form>
            </div>
            <div class="container">
                <div class="row">
                    <div class="ma mt-3">
                        <button class="btn btn-dark" type="submit" form="this-form">Logar</button>
                    </div>
                </div>
            </div>
        </main>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"sign-in-styles.css"
def css():
    """
    body {background-color: #171A21; color: #0e3742;}
    .container-fluid {position: fixed; top: 0; background-color: #171A21;} /* cor de fundo deve ser = body */
    .btn-dark:hover a {text-decoration: none;}
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
