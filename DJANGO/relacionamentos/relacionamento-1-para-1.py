

"""
Objetivo:
         exemplificar uso do campo de modelo do tipo: [ OneToOneField ]
Exemplo:
        1. /home/lucas/PycharmProjects/models_foreignkey_manytomany_onetomany
        2. recursos/DJANGO/m/models_foreignkey_manytomany_onetoone.py
"""

def fonte():
    """
    Curso # Programação Web com Python e Django framework: Essencial
    Local # Seção 9:Relacionamentos entre modelos
    Aula  # 80. Relacionamento Um para Um
    """

def terminal():
    """
    pip install django
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

"Modelos que servem como [ OneToOneField ] normalmente possuem somente 1 campo"
def models():
    """
    class Chassi(models.Model):
        number = models.CharField('Chassi', help_text='máx. 16 chars', max_length=16)

        class Meta:
            verbose_name = 'Chassi'
            verbose_name_plural = 'Chassis'

        def __str__(self):
            return self.number

    class Vehicle(models.Model):
        chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
        name = models.CharField('Modelo', help_text='máx. 50 chars', max_length=50)
        price = models.DecimalField('Preço', decimal_places=2, help_text='máx. 7 dígitos e 2 casas decimais', max_digits=9)

        class Meta:
            verbose_name = 'Veículo'
            verbose_name_plural = 'Veículos'

        def __str__(self):
            return self.name
    """

def admin():
    """
    from django.contrib import admin
    from .models import Chassi, Vehicle

    @admin.register(Chassi)
    class ChassiAdmin(admin.ModelAdmin):
        list_display = ('number',)

    @admin.register(Vehicle)
    class VehicleAdmin(admin.ModelAdmin):
        list_display = ('chassi', 'name', 'price')
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

def template_admin():
    """
    1 - Os dois modelos tornam-se interdependentes: [ Chassi ] & [ Vehicle ]
    2 - O modelo Chassi precisa ter pelo menos 1 objeto criado, para ser passado como opção no outro modelo: Vehicle
    3 - O lógica é: 1 chassi para 1 veículo (pois cada veículo só pode ter um chassi)
    4 - Nesse lógica, é também uma opção, substituir [ OneToOneField ] por [ ForeignKey ]
    """

"Campos originais"  # name / price >>> SINTAXE: var_objeto.campo_local
"Campo herdado"     # chassi       >>> SINTAXE: var_objeto.campo_local.campo_original
def terminal3():
    """
    python manage.py shell
    from pa.models import *
    var = Vehicle.objects.get(name='Ultran')
    var.name          # 'Ultran'
    var.price         # Decimal('29414.00')
    var.chassi        # <Chassi: 1009413>
    var.chassi.number # 1009413

    SE HOUVESSEM OUTROS CAMPO, COMO [ ForeignKey ]

    var.drivers                # <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f52d9b33b80>
    var.drivers.all()          # <QuerySet [<User: mario>]>
    var.drivers.all()[0]       # <User: mario>]
    str(var.drivers.all()[0])  # 'mario'
    """
