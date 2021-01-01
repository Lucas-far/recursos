

"""
Módulo >>> menu.py

Objetivo:
         criar um menu responsivo para tela menor e maior
"""

def templates():
    """
    <!DOCTYPE html>
    {% load static %}
    {% load bootstrap4 %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/menu.css' %}" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta charset="UTF-8">
        <title>Página ínicial</title>
    </head>
    <body>

        <!--Barra de navegação para resolução média ou acima-->
        <div class="container-fluid">
            <nav class="nav-first">
                <div class="row text-center ma mt-2 mb-4">
                    <span class="col-12 col-sm-12 col-md-2 col-lg-2 col-xl-2"><a class="my-nav" href="#">Item 1</a></span>
                    <span class="col-12 col-sm-12 col-md-2 col-lg-2 col-xl-2"><a class="my-nav" href="#">Item 2</a></span>
                    <span class="col-12 col-sm-12 col-md-2 col-lg-2 col-xl-2"><a class="my-nav" href="#">Item 3</a></span>
                    <span class="col-12 col-sm-12 col-md-2 col-lg-2 col-xl-2"><a class="my-nav" href="#">Item 4</a></span>
                    <span class="col-12 col-sm-12 col-md-2 col-lg-2 col-xl-2"><a class="my-nav" href="#">Item 5</a></span>
                </div>
            </nav>
        </div>

        <!--Barra de navegação para resolução muito pequena até pequena-->
        <div class="container nav-second">
            <div class="row">
                <div class="nav-item dropdown col-12 col-sm-12 col-md-2 col-lg-2 col-xl-2 ma">
                    <button class="btn btn-dark my-btn">
                        <a aria-expanded="false" aria-haspopup="true"
                           class="nav-link dropdown-toggle my-a"
                           data-toggle="dropdown" href="#" id="navbarDropdown" role="button">Menu
                        </a>
                        <span aria-labelledby="navbarDropdown" class="dropdown-menu">
                            <a class="dropdown-item" href="#">Item 1</a>
                            <a class="dropdown-item" href="#">Item 2</a>
                            <a class="dropdown-item" href="#">Item 3</a>
                            <a class="dropdown-item" href="#">Item 4</a>
                            <a class="dropdown-item" href="#">Item 5</a>
                        </span>
                    </button>
                </div>
            </div>
        </div>

        <main>
            <a class="a" href="#">Texto</a><a class="a" href="#">Texto</a><a class="a" href="#">Texto</a>
            <a class="a" href="#">Texto</a><a class="a" href="#">Texto</a><a class="a" href="#">Texto</a>
            <a class="a" href="#">Texto</a><a class="a" href="#">Texto</a><a class="a" href="#">Texto</a>
            <a class="a" href="#">Texto</a><a class="a" href="#">Texto</a><a class="a" href="#">Texto</a>
            <a class="a" href="#">Texto</a><a class="a" href="#">Texto</a><a class="a" href="#">Texto</a>
        </main>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css():
    """
    body {background-color: #222; color: white;}

    /* Configuração do menu grande */
    .nav-first {
        position: fixed;
        top: 0;
        background-color: #292929;
        width: 97%;
        padding: 15px 0 0 0;
        box-shadow: 0 0 5px #128c7e, 0 0 15px #128c7e, 0 0 25px #128c7e;
    }

    /* Nomes dos itens do menu grande */
    .my-nav {transition: .5s; color: black;}

    .my-nav:hover {
        border-top: #128c7e solid 5px;
        border-bottom: #128c7e solid 5px;
        padding: 10px;
        border-radius: 50%;
        color: #128c7e;
        text-decoration: none;
    }

    .my-a {font-size: 1.5em;}

    /* Configuração do menu pequeno */
    .container {background-color: #222;} /* impedir que o conteúdo que passa pelo menu fixo, seja visto acima */
    .nav-second {position: fixed; top: 0; left: 0;}
    .my-btn {font-size: .5em;}
    .my-btn a {color: black;}
    .btn-dark:hover a {text-decoration: none;}
    .dropdown-item {text-align: right; padding: 20px 0 0 -5px;}
    .dropdown-menu {background-color: #292929; width: 200%;}

    /* Global */
    .ma {margin: auto;}

    /* Outros */
    main {margin-top: 200px;}

    /* Conteúdo adicionado para testar rolagem e sobreposição */
    .a {display: block; font-size: 5em; text-align: center;}

    /* até à resolução de 768px, o menu grande é escondido */
    @media screen and (max-width: 768px) {.nav-first {visibility: hidden;}}

    /* a partir da resolução de 768px, o menu pequeno é escondido */
    @media screen and (min-width: 768px) {.nav-second {visibility: hidden;}}
    """
