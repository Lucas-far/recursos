

"""
Objetivo:
         mostrar a diferença entre uso de objeto com métodos [ filter ] vs [ get ]
"""

def declarar():
    """
    python manage.py shell
    from pa.models import *
    eu = Modelo.objects.filter(nome='Lucas Santos')
    eu2 = Modelo.objects.get(nome='Lucas Santos')
    """

"filter"  # <class 'django.db.models.query.QuerySet'>
"get"     # <class 'pa.models.Modelo'>
def diferente():
    """
    1. eu
       <QuerySet [<Modelo: Lucas Santos>]>

    2. eu2
       <Modelo: Lucas Santos>
    """

"filter"  # permite iteração
"get"     # não permite iteração
def diferente2():
    """
    7.
        for obj in eu:
            print(obj)
    Lucas Santos

    8.
        for obj in eu2:
            print(obj)

        Traceback (most recent call last):
        File "<console>", line 1, in <module>
        TypeError: 'Modelo' object is not iterable
    """

"filter"  # não acessa campos (apenas por indexação)
"get"     # acessa campos
def diferente3():
    """
    9. eu.nome

       Traceback (most recent call last):
       File "<console>", line 1, in <module>
       AttributeError: 'QuerySet' object has no attribute 'nome'

    9. eu[0] >>> <Modelo: Lucas Santos>

    10. eu2.nome >>> 'Lucas Santos'
    """

"filter"  # não altera
"get"     # altera campos por objeto.campo
def diferente4():
    """
    eu[0] >>> <Modelo: Lucas Santos>
    eu[0] = 'Santos Lucas'

        Traceback (most recent call last):
        File "<console>", line 1, in <module>
        TypeError: 'QuerySet' object does not support item assignment

    eu2.nome >>> 'Lucas Santos'
    eu2.nome = 'Alfredo Fredoal'
    eu2.nome >>> 'Alfredo Fredoal'
    """

def declarar2():
    """
    f = Interview.objects.filter(full_name='Pessoa1')
    g = Interview.objects.get(full_name='Pessoa1')
    """

"filter"  # mostra objetos por método .values()
"get"     # mostra objetos por método .__dict__
def diferente5():
    """
    f.values()

    <QuerySet [
        {'id': 9, 'full_name': 'Pessoa1', 'email': 'pessoa1@gmail.com', 'age': 25, 'gender': 'feminino',
         'nationality': 'Brasileiro', 'brief_description': 'Eu faço bolo de milho', 'self_grade': Decimal('6.9'),
          'passtimes': 'Cantar', 'slug': 'pessoa1', 'avatar': 'database_interview/IMG-20201211-WA0002_1.jpg'}
    ]>

    f.values()[0]

        {'id': 9, 'full_name': 'Pessoa1', 'email': 'pessoa1@gmail.com', 'age': 25, 'gender': 'feminino',
         'nationality': 'Brasileiro', 'brief_description': 'Eu faço bolo de milho', 'self_grade': Decimal('6.9'),
          'passtimes': 'Cantar', 'slug': 'pessoa1', 'avatar': 'database_interview/IMG-20201211-WA0002_1.jpg'}

    f.values()[0][]

    g.__dict__

    {'_state':
        <django.db.models.base.ModelState object at 0x7fd2c2c7c790>, 'id': 9, 'full_name': 'Pessoa1',
        'email': 'pessoa1@gmail.com', 'age': 25, 'gender': 'feminino', 'nationality': 'Brasileiro',
        'brief_description': 'Eu faço bolo de milho', 'self_grade': Decimal('6.9'), 'passtimes': 'Cantar',
        'slug': 'pessoa1', 'avatar': <StdImageFieldFile: database_interview/IMG-20201211-WA0002_1.jpg>
    }
    """
