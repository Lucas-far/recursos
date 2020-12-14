

from django.template.defaultfilters import slugify

def infos():
    """
    Objetivo
         converter campos de um modelo string composto, com espaçamento de traço entre cada palavra

    Observação
        1. é mais conveniente usar esse método com campos cujo valor seja um string
    """

def declarar():
    exemplo = slugify('Lucas Farias Santos de Sousa')
    print('declaração =', exemplo)
    # declaração = lucas-farias-santos-de-sousa

def print_():
    print('print =', slugify({'Django é um framework Python!'}))
    # print = django-e-um-framework-python

def redeclarar():
    exemplo = {'Nome': 'Elain', 'Sobrenome': 'não informado'}
    exemplo = slugify(exemplo)
    print('redeclaração =', exemplo)
    # redeclaração = nome-elain-sobrenome-nao-informado

def var_nova():
    exemplo = ['Você usa', 'Django', '?']
    exemplo2 = slugify(exemplo)
    print('variável nova =', exemplo2)
    # variável nova = voce-usa-django

declarar(), print_(), redeclarar(), var_nova()
