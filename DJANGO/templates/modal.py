

"""
Objetivo:
         construir um botão modal para exibir dados aninhado à uma página
"""

def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/modal.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página de um modal</title>
    </head>
    <body>
        <button class="btn btn-primary" data-target="#staticBackdrop" data-toggle="modal" type="button">
            Descrição do botão modal
        </button>
        <div aria-hidden="true" aria-labelledby="staticBackdropLabel" class="modal fade" data-backdrop="static"
             data-keyboard="false" id="staticBackdrop" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">Descrição</h5>
                    </div>
                    <div class="modal-body">
                        <span>Você deseja, de fato, deletar esta tarefa?</span>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-secondary" data-dismiss="modal" type="button">Fechar</button>
                    </div>
                </div>
            </div>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css():
    """
    .modal-dialog {color: dimgray;}
    .modal-header {letter-spacing: 4px;}
    .modal-header, .modal-body, .modal-footer {background-color: #222; border: #292929 solid 1px;}
    """
