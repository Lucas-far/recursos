

from typing import Union

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 170. Debugger mais simples com f-strings
    """

def infos():
    """
    Objetivo
        alterar a exibição de dados numéricos em string
    """

def elevar(um: Union[int, float], dois: Union[int, float]) -> Union[int, float]:
    return um ** dois

objeto: Union[int, float] = elevar(9.47, 7)
print(f'Resultado: {objeto:.1f}')                   # Usando objeto
print(f'Resultado: {elevar(4, 7.88):.1f}')          # Usando literal
print('Resultado: {:.2f}'.format(objeto))           # Usando objeto
print('Resultado: {:.2f}'.format(elevar(4, 7.88)))  # Usando literal
