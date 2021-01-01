

"""
Módulo: add_javascript.py

Objetivo:
         exemplificar formas de uso de funções js
"""

def exemplo():
    """
    function mensagem() {
        alert('Python = Cobra\nDjango = Unicórnio');
    }
    """

def exemplo2():
    """
    function perguntar() {
        var name;
        name = prompt('Informe-nos o seu nome');
        alert('Obrigado por informar, ' + name + '.');
    }
    """

def exemplo3():
    """
    function variar() {
        let change_tag = document.getElementsByTagName('h2');

        if
        (change_tag[0].innerText == 'Página Inicial')
        {change_tag[0].innerText = 'Página JavaScript';}
        else
        {change_tag[0].innerText = 'Página Inicial';}
    }
    """

def exemplo4():
    """
    function incrementar() {
        let counter = document.getElementById('contador')
        counter.innerText = parseInt(counter.innerText) + 1;
    }
    """

"OBS"                # Funções js podem ser ou não chamadas dentro de uma tag de botão
"<script></script>"  # mandatória
def body():
    """
    <body>
        <button onclick="mensagem();">Mostrar mensagem</button>
        <button onclick="perguntar();">Responder perguntas</button>
        <button onclick="variar();">Mudar texto principal</button>
        <button onclick="incrementar();">Contar</button>
        <p id="contador">0</p>
        <script type="text/javascript" src="{% static 'js/scripts.js' %}"></script>
    </body>
    """
