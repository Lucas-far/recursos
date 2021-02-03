

"""
Módulo: if_name_main.py
Objetivo: impedir conflitos de teste de métodos, caso este seja usado em mais de um local
Objetivo 2: mostrar a sintaxe que resolve problema de conflitos de teste de métodos
"""

# sintaxe
"OBS"  # no seu escopo, são testados métodos escritos no arquivo
def parte_1():
    """
    if __name__ == '__main__':
        pass
    """

# Exemplo de um método escrito neste arquivo
def convert_dict_to_tuple(key='key', value='value'):
    """"""
    return tuple({key: value}.items())

# Uso prático da sintaxe, que guarda os testes
"OBS"  # se o método fosse testado fora deste escopo, este estaria exposto a problemas
"OBS"  # o principal problema está caso este método fosse importado em outro arquivo, para ser reutilizado
"OBS"  # qualquer teste feito, refletiria também onde o método fosse chamado, prejudicando a legibilidade
if __name__ == '__main__':
    print(convert_dict_to_tuple())
