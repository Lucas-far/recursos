

"""
Módulo >>> html_class.py

Objetivo:
         exemplificar usos de classes, que alteram comportamentos no template
"""

def btn():
    """
    <button type="button" class="btn btn-primary">botão azul claro</button>
    <button type="button" class="btn btn-secondary">botão cinza escuro</button>
    <button type="button" class="btn btn-success">botão verde claro</button>
    <button type="button" class="btn btn-danger">botão salmão</button>
    <button type="button" class="btn btn-warning">botão amarelo queimado</button>
    <button type="button" class="btn btn-info">botão azul cião</button>
    <button type="button" class="btn btn-light">botão branco</button>
    <button type="button" class="btn btn-dark">botão preto fosco</button>
    <button type="button" class="btn btn-link">botão de link comum transparente</button>
    """

    # Se o seu botão for de formato apenas link (sem tag <button></button>), insira a classe: role="button"
    """ <a class="btn btn-primary" href="#" role="button">Link</a> """

def mb():
    """
    Referência:
               {margin-bottom:;}

    <tag class="mb-1 mb-2 mb-3 mb-4 mb-5"></tag>
    """

def mt():
    """
    Referência:
               {margin-top:;}

    <tag class="mt-1 mt-2 mt-3 mt-4 mt-5"></tag>
    """

def form_control():
    """
    Objetivo:
             estilização do campo de formulário, inserido na tag <input>

    <form id="this-form" method="post">
        {% csrf_token %}
        <label class="sr-only" for="username">Descrição leitor de tela</label>
        <input class="form-control mb-2" id="username" name="username" placeholder="e-mail" type="email" required>

        <label class="sr-only" for="password">Descrição leitor de tela</label>
        <input class="form-control" id="password" name="password" placeholder="senha" type="password" required>

        <button class="btn btn-block btn-lg btn-warning" form="this-form" type="submit">login/entrar</button>
        <p class="mt-2 text-muted">&copy; {% now 'Y' %}</p>
    </form>
    """

def form_signin():
    """
    Objetivo:
             layout de campos com tamanho pré-definido para formulários, normalmente formulários de login

    <form class="form-signin"></form>
    """

def sr_only():
    """
    Objetivo:
             esconder textos em tags textuais, tornando-os disponíveis somente para leitores de tela

    <h2 class="sr-only">Eu estou escondido</h2>
    """

def table():
    """
    Objetivo:
             estilizar tabelas e seus componentes

    table
    table table-bordered
    table table-bordered table-dark
    table table-borderless
    table table-borderless table dark
    table table-dark
    table table-hover
    table table-hover table-dark
    table table-sm
    table table-sm table-dark
    table table-striped
    table table-striped table-dark

    Exemplo:
            <table class="table table-bordered table-dark"></table>
    """

def thead():
    """
    Objetivo:
             estilizar elementos de cabeçalho de uma tabela

    thead-dark
    thead-light

    Exemplo:
            <table>
                <thead class="thead-dark">
                    <tr>
                        <th></th>
                    </tr>
                </thead>
            </table>
    """

def text_right_text_left_text_center():
    """
    Objetivo:
             alinhamento de conteúdo, funcionando somente se a classe for inserida dentro de uma tag <div></div>

    Exemplo ERRADO:
                   <span class="container text-right">SPAN</span>

    Exemplo CORRETO:
                    <div class="text-center"><span>centro</span></div>
                    <div class="text-left"><span>centro</span></div>
                    <div class="text-right"><span>centro</span></div>
    """
