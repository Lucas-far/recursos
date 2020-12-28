

# bootstrap não obrigatório, mas whitenoise pode é útil para ver os templates no modo produção
def terminal():
    """
    pip install django-bootstrap4
    pip install whitenoise
    """

# INSTALLED_APPS pode ser ignorada, caso bootstrap não tenha sido inserido
def settings():
    """
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['bootstrap4']
    DEBUG = False
    MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
    """

# var = 'nome_pacote_aplicação.módulo.nome_view'
def pp_urls():
    """
    handler404 = 'pa.views.handler404'
    handler500 = 'pa.views.handler500'
    """

def views():
    """
    def handler404(request, exception):
        return render(request, '404.html')

    def handler500(request):
        return render(request, '500.html')
    """

def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página não encontrada</title>
        <style>
            body {background-image: linear-gradient(to right, #1da1f2, #14171a); color: silver;}
            hr {background-color: #c32aa3; height: 3px; box-shadow: 0 0 50px #c32aa3; border-radius: 10px;}
        </style>
    </head>

    <body>
        <div class="container mt-5">
            <h3>A rota da página requisitada não existe, ou foi digitada incorretamente</h3>
            <hr>
            <a class="btn btn-light" href="{% url 'index' %}">Voltar à página inicial</a>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """
