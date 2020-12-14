

from collections import Counter
from random import choice

def infos():
    """
    Objetivo
        impedir o uso, em funções, de argumento nomeados (keyword arguments)

    Objetivo 2
        obrigar o uso, em funções, de argumento nomeados (keyword arguments)

    Objetivo 3
        misturar o uso, em funções, entre ser ou não obrigatório o uso de argumentos nomeados (keyword arguments)

    Observações
        funções sem permissão de argumento nomeado, recebem /, que sempre devem ser o último elemento a direita
    """

# Função normal
def criar_dicio(chave, valor):
    return {chave: valor}
print(criar_dicio(chave='linguagem', valor='Python'))

# Função objetivo 1
def texto_invertido(texto: str, /):
    print(texto[::-1])
texto_invertido('Eu não sei o que dizer')
# texto_invertido(texto='Eu não sei o que dizer')
"TypeError: texto_invertido() got some positional-only arguments passed as keyword arguments: 'texto'"

# Função objetivo 2
def contar_letras(*, texto: str):
    texto = dict(Counter(texto))
    print(texto)
contar_letras(texto='Vá se lascar, sua porra!')
# contar_letras('Vá se lascar, sua porra!')
"TypeError: contar_letras() takes 0 positional arguments but 1 was given"

# Função objetivo 2
def dar_adjetivo(*, nome, sobrenome):
    adjetivos = [
        'viado(a)', 'arrombado(a)', 'travesti', 'machista', 'taxista', 'comunista', 'pedreiro(a)', 'drogado(a)'
    ]
    print(f'{nome + " " + sobrenome}, você é um tremendo {choice(adjetivos)}')
dar_adjetivo(nome='Lucas', sobrenome='Alfredo')
# dar_adjetivo('Lucas', sobrenome='Alfredo')
"TypeError: dar_adjetivo() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument)"

# Função objetivo 3
def mensagem(email, /, assunto='Não especificado', *, texto):
    print(
        f"""
        ========== Opinião do usuário ==========
        {email}
        {assunto}
        {texto}
        """
    )

mensagem('lalala@gmail.com', 'Ratos', texto='Os ratos são primos dos esquilos')
# mensagem(email='lalala@gmail.com', 'Ratos', texto='Os ratos são primos dos esquilos')
"SyntaxError: positional argument follows keyword argument"
# mensagem('lalala@gmail.com', 'Os ratos são primos dos esquilos')
"TypeError: mensagem() missing 1 required keyword-only argument: 'texto'"
