

"""
Módulo >>> modelo_base.py

Objetivo:
         modelo que serve parar ser herdado, com informações globais, como: de data, tempo e disponibilidade
"""

"abstract"  # Torna esse modelo indisponível para receber migração, pois isto é desnecessário
def models():
    """
    from django.db import models

    class Base(models.Model):
        creation = models.DateTimeField('Data de criação', auto_now_add=True)
        updated = models.DateTimeField('Última atualização', auto_now=True)
        availability = models.BooleanField('Disponível', default=True)

        class Meta:
            abstract = True
    """
