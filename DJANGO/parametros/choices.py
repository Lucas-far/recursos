

"""
Objetivo:
         criar campos de escolha em modelos

Exemplo:
        recursos/DJANGO/e/email_backend.py
        /home/lucas/PycharmProjects/email_backend
"""

def tutorial():
    """
    1 - Inicia-se no escopo do modelo, com a criação de uma tupla, com tuplas aninhadas

        EXEMPLO:
                choices_colors = (
                    ('azul', 'azul'), ('amarelo', 'amarelo'), ('vermelho', 'vermelho')
                )

    2 - Essa tupla, por convenção, deve ter uma sintaxe: choices_nome_do_campo
    3 - Após a tupla estar criada, esta é passada como argumento de um parâmetro chamado: choices
    4 - O campo que recebe o parâmetro choices, normalmente recebe 3 parâmetros: Título, choices=, max_length=
    5 - O parâmetro max_length= refere-se a quantidade de caracteres maior que há na tupla
    5 - Por exemplo, na tupla criada acima [ choices_colors ] 'vermelho' é o maior índice, com 8 caracteres
    5 - Sendo assim: max_length=8

        EXEMPLO: campo = models.Charfield('Título', choices=choices_nome_do_campo, max_length=int)
    """
