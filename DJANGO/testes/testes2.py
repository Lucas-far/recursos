

"""
Módulo >>> testes2.py

Objetivo:
         exemplificar uma maneira de teste menos comuns para projetos Django
"""

def fonte():
    """
    Curso  # Programação Web com Python e Django framework: Essencial
    Seção  # Seção 6:Testando seu projeto
    Aula   # 60. Testando models
    """

def terminal():
    """
    pip install coverage
    """

"==============="
# Primeiro teste
"==============="

def models():
    """
    from django.db import models

    class Name(models.Model):
        full_name = models.CharField('Nome completo', max_length=100)

        class Meta:
            verbose_name = 'Nome completo'
            verbose_name_plural = 'Nomes completos'

        def __str__(self):
            return self.full_name
    """

# Exemplo de teste menos eficiente
def teste_models_regular():
    """
    from pa.models import *
    from django.test import TestCase

    class NameTestCase(TestCase):

        def setUp(self):
            self.var = str(Name.objects.create(full_name='Ricardo Armando'))

        def test_name(self):
            var = Name.objects.get(full_name='Ricardo Armando')
            self.assertEqual(self.var, var.__str__())
    """

# Exemplo de teste mais eficiente
def teste_models_bom():
    """
    from pa.models import *
    from django.test import TestCase
    from model_mommy import mommy

    class ModelNameTestCase(TestCase):
        def setUp(self):
            self.var = mommy.make('Name')

        def test_str(self):
            self.assertEquals(str(self.var), self.var.full_name)
    """

"=============="
# Segundo teste
"=============="

def models2():
    """
    class Age(models.Model):
        age = models.IntegerField('Idade')

        class Meta:
            verbose_name = 'Idade'
            verbose_name_plural = 'Idades'

        def __str__(self):
            return str(self.age)
    """

# Exemplo de teste menos eficiente
def teste_models2_regular():
    """
    from pa.models import *
    from django.test import TestCase

    class AgeTestCase(TestCase):

        def setUp(self):
            self.var = str(Age.objects.create(age=18))

        def test_age(self):
            var = Age.objects.get(age=18)
            self.assertEqual(self.var, var.__str__())
    """

# Exemplo de teste mais eficiente
def teste_models2_bom():
    """
    from pa.models import *
    from django.test import TestCase
    from model_mommy import mommy

    class ModelAgeTestCase(TestCase):
        def setUp(self):
            self.var = mommy.make('Age')

        def test_str(self):
            self.assertEquals(str(self.var), str(self.var.age))
    """

"==============="
# Terceiro teste
"==============="

def models3():
    """
    class Address(models.Model):
        neighborhood = models.CharField('Nome do bairro', max_length=150)
        street = models.CharField('Nome da rua', max_length=150)
        house = models.IntegerField('Número da casa')

        class Meta:
            verbose_name = 'Endereço'
            verbose_name_plural = 'Endereços'

        def __str__(self):
            return self.neighborhood
    """

# Exemplo de teste menos eficiente
def teste_models3_regular():
    """
    from pa.models import *
    from django.test import TestCase

    class AddressTestCase(TestCase):

        def setUp(self):
            self.var = str(Address.objects.create(neighborhood='Poty Velho', street='João Palmeiras', house=37))

        def test_age(self):
            var = Address.objects.get(neighborhood='Poty Velho')
            self.assertEqual(self.var, var.__str__())
    """

# Exemplo de teste mais eficiente
def test_models3_bom():
    """
    from pa.models import *
    from django.test import TestCase
    from model_mommy import mommy

    class ModelAddressTestCase(TestCase):
        def setUp(self):
            self.var = mommy.make('Address')

        def test_str(self):
            self.assertEquals(str(self.var), self.var.neighborhood)
    """

# Executando os testes
def terminal2():
    """
    python manage.py test
    coverage run manage.py test
    """
