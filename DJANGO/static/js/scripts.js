

function mensagem() {
    alert('Python = Cobra\nDjango = Unicórnio');
}

function perguntar() {
    var name;
    name = prompt('Informe-nos o seu nome');
    alert('Obrigado por informar, ' + name + '.');
}

function variar() {
    let change_tag = document.getElementsByTagName('h2');

    if
    (change_tag[0].innerText == 'Página Inicial')
    {change_tag[0].innerText = 'Página JavaScript';}
    else
    {change_tag[0].innerText = 'Página Inicial';}
}

function incrementar() {
    let counter = document.getElementById('contador')
    counter.innerText = parseInt(counter.innerText) + 1;
}