

"""
Módulo >>> queryset.py

Objetivo:
         exemplificar um queryset de um modelo e como fazer uso dele
"""

def terminal():
    """
    python manage.py shell
    from pa.models import *
    q = Interview.objects.all().values()
    q

        <QuerySet [
            {'id': 10, 'full_name': 'Pessoa2', 'email': 'pessoa2@gmail.com', 'age': 21, 'gender': 'masculino',
             'nationality': 'Brasileiro', 'brief_description': 'Eu gosto da cor amarela', 'self_grade': Decimal('8.0'),
              'passtimes': 'Pular corda', 'slug': 'pessoa2', 'avatar': 'database_interview/scorpion.png'},
            {'id': 9, 'full_name': 'Pessoa1', 'email': 'pessoa1@gmail.com', 'age': 25, 'gender': 'feminino',
             'nationality': 'Brasileiro', 'brief_description': 'Eu faço bolo de milho', 'self_grade': Decimal('6.9'),
             'passtimes': 'Cantar', 'slug': 'pessoa1', 'avatar': 'database_interview/IMG-20201211-WA0002_1.jpg'}
        ]>

    q[0]['id']        >>> 10
    q[0]['full_name'] >>> 'Pessoa2'
    q[1]['email']     >>> 'pessoa1@gmail.com'
    q[1]['age']       >>> 25
    """
