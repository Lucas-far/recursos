

"""
Módulo >>> models_foreignkey_manytomany_onetoone.py

Objetivo:
         explicar o uso dos campos: [ models.ForeignKey ] [ models.ManyToManyField ] [ models.OneToManyField ]
Fonte:
      /home/lucas/PycharmProjects/models_foreignkey_manytomany_onetomany
"""

# todo Nome do av escrito erroneamente, sendo o certo: models_foreignkey_manytomany_onetoone

def fonte():
    """
    Curso # Programação Web com Python e Django Framework: Essencial
    Seção # Seção 9:Relacionamentos entre modelos
    Aula  # 83. Aproveitando os recursos do Django Models
    """

def terminal():
    """
    pip install django==2.2.17 django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

"OBS"             # campos do tipo [ ForeignKey ] [ ManyToMany ] [ OneToMany ] [ ManyToMany ] tendem a ter só 1 campo
"OBS2"            # parece que [ ForeignKey ] é similiar a = [ OneToMany ]
"Manufacturer"    # Modelo que gera [ models.Foreignkey ]
"Manufacturer"    # modelo que contém um campo, que recebe como opção, objetos de um campo de outro modelo já criados
"Manufacturer"    # LÓGICA: um veículo para vários fabricantes
"get_user_model"  # Modelo que gera [ models.ManyToManyField ], dando acesso ao bdd padrão Django [ User ]
"get_user_model"  # modelo que contém um campo, que recebe como opção, objetos de usuário do modelo [ User ]
"get_user_model"  # LÓGICA: vários veículos dirigidos por vários motoristas
"Chassi"          # Modelo que gera [ models.OneToOneField ]
"Chassi"          # modelo que contém um campo, que recebe como opção, objetos de outro modelo já criados
"Chassi"          # LÓGICA: cada veículo pode ter 1 chassi
def models():
    """
    from django.db import models
    from django.contrib.auth import get_user_model

    class Chassi(models.Model):
        number = models.CharField('Chassi', help_text='máx. 7 chars', max_length=7)

        class Meta:
            verbose_name = 'Chassi'
            verbose_name_plural = 'Chassis'

        def __str__(self):
            return self.number

    class Manufacturer(models.Model):
        name = models.CharField('Nome', help_text='máx 50 chars', max_length=50)

        class Meta:
            verbose_name = 'Fabricante'
            verbose_name_plural = 'Fabricantes'

        def __str__(self):
            return self.name

    class Vehicle(models.Model):
        name = models.CharField('Nome', help_text='máx. 50 chars', max_length=50)
        price = models.DecimalField('Preço', help_text='máx. 7 dígitos e 2 casas decimais', decimal_places=2, max_digits=9)
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_DEFAULT, default='Fabricante deletado')
        drivers = models.ManyToManyField(get_user_model())
        chassi = models.OneToOneField(Chassi, on_delete=models.SET_DEFAULT, default='Chassi deletado')

        class Meta:
            verbose_name = 'Veículo'
            verbose_name_plural = 'Veículos'

        def __str__(self):
            return self.name
    """

"Um campo ManyToManyField não pode ser passado diretamente no módulo [ admin.py ]"  # Vehicle.drivers
"Para corrigir, faz-se um método com uma lógica comprehension"                      # def show_field_drivers
def admin():
    """
    from django.contrib import admin
    from .models import Chassi, Manufacturer, Vehicle

    @admin.register(Chassi)
    class ChassiAdmin(admin.ModelAdmin):
        list_display = ('number',)

    @admin.register(Manufacturer)
    class ManufacturerAdmin(admin.ModelAdmin):
        list_display = ('name',)

    @admin.register(Vehicle)
    class VehicleAdmin(admin.ModelAdmin):
        list_display = ('name', 'price', 'show_field_drivers')

        def show_field_drivers(self, obj):
            return ', '.join([each_data.username for each_data in obj.drivers.all()])
        show_field_drivers.short_description = 'Motoristas'
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

"Ir ao template admin e criar objetos, mas como temos campos interdependentes, é preciso seguir uma ordem"
"1 - Cria-se objetos para o modelo: Chassi"       # OneToOneField
"2 - Cria-se objetos para o modelo Manufacturer"  # ForeignKey
"3 - Então, será possível ver a influência dos campos interdependentes sob o modelo Vehicle"
