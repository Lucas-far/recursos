

"""
Módulo >>> model_form_postgresql.py

Objetivo:
         usar um formulário modelo a partir de um bdd

Fonte:
      /home/lucas/PycharmProjects/django_model_form

OBS:
    será usado uma configuração baseada no postgresql
"""

def pgadmin4():
    """
    1. Abrir o software Pgadmin4
    2. Inserir senha do OS
    3. Inserir senha da conta
    4. Pós carregamento -> [ Botão direito ] [ Databases ] [ Create ] [ Database ] [ Name = dtb_django_model_form ]
    """

"pip install django-stdimage"  # não obrigatório (usado como campo de upload de imagem do modelo)
def terminal():
    """
    pip install django==2.2.17 django-bootstrap4 django-stdimage psycopg2-binary whitenoise
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = {'DIRS': ['templates']}
    MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bddpostgresql',     # única chave com valor livre
            'USER': 'luksadmin',         # nome do usuário novo criado após a criação do usuário padrão 'root'
            'PASSWORD': 'passwort2772',  # senha configurada junto com o usuário novo
            'HOST': 'localhost',         # valor padrão
            'PORT': '5432',              # valor apdrão
        }
    }
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

# todo INÍCIO - Configuração de SLUG
"Um formulário modelo inicia-se através da criação de um modelo"
def models():
    """
    from django.db import models
    from stdimage import StdImageField
    from django.template.defaultfilters import slugify
    from django.db.models import signals


    class Interview(models.Model):
        choices_gender = (('feminino', 'feminino'), ('masculino', 'masculino'), ('outro', 'outro'))

        full_name = models.CharField('Nome completo', max_length=200, default='Francisco Farias')
        email = models.EmailField('E-mail', max_length=200, default='email@domínio.com')
        age = models.IntegerField('Idade', default=18)
        gender = models.CharField('Gênero', choices=choices_gender, max_length=9, default=None)
        nationality = models.CharField('Nacionalidade', max_length=100, default='Turco')
        brief_description = models.TextField('Conte algo sobre você', default='Escreva aqui.')
        self_grade = models.DecimalField('Sua nota sincera auto-avaliativa', decimal_places=1, max_digits=3)
        passtimes = models.CharField('Conte alguns de seus passatempos', max_length=500)
        slug = models.SlugField('Slug', blank=True, editable=False, max_length=200)

        avatar = StdImageField(
            'Avatar',
            upload_to='database_other',
            variations={'Thumb': {'height': 500, 'width': 500, 'crop': True}}
        )

        class Meta:
            verbose_name = 'Pessoa'
            verbose_name_plural = 'Pessoas'

        def __str__(self):
            return self.email

    def slug_database_interview(instance, **kwargs):
        instance.slug = slugify(instance.full_name)

    signals.pre_save.connect(slug_database_interview, sender=Interview)
    """
# todo FIM - Configuração de SLUG

def admin():
    """
    from django.contrib import admin
    from .models import Interview

    @admin.register(Interview)
    class OtherAdmin(admin.ModelAdmin):
        list_display = (
            'full_name', 'email', 'age', 'gender', 'nationality',
             'brief_description', 'self_grade', 'passtimes', 'avatar'
        )
    """

"O modelo criado precisa ter uma versão sua, em forma de formulário"
"slug"  # campo que não deve ser adicionado, pois ele não é criado diretamente pelo usuário
def pa_forms():
    """
    from django import forms
    from .models import Interview

    class InterviewModelForm(forms.ModelForm):
        class Meta:
            model = Interview
            fields = (
                'full_name', 'email', 'age', 'gender', 'nationality',
                'brief_description', 'self_grade', 'passtimes', 'avatar')
    """

# todo Formulário function based view
def views():
    """
    from django.contrib import messages
    from django.shortcuts import redirect
    from django.shortcuts import render
    from .forms import InterviewModelForm

    def interview(request):
        model_form = InterviewModelForm(request.POST or None, request.FILES)

        if str(request.method) == 'POST':
            if model_form.is_valid():
                model_form.save()
                messages.success(request, 'Formulário preenchido com sucesso. Obrigado por participar!')
                return redirect('index')
            else:
                messages.error(request, 'Houve algum erro em um dos campos do formulário')
        else:
            model_form = InterviewModelForm()

        context = {'model_form': model_form}
        return render(request, 'interview.html', context)
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [path('', index, name='index'), path('interview/', interview, name='interview')]
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """

"fixed-return-button.html"  # template global para: [ interview.html ], [ interview2.html ], [ interview3.html ]
def templates():
    """
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <a class="btn btn-primary" href="{% url 'index' %}">Voltar à página Inicial</a>
            </div>
        </div>
    </div>
    """

"index.html"
def templates2():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="#" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página inicial</title>
    </head>
    <body>
        {% bootstrap_messages %}
        <h2>Página inicial</h2>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"interview.html"
def templates3():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/interview-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Formulário de entrevista</title>
    </head>
    <body>
        {% include 'fixed-return-button.html' %}
        <div class="container">
            <form autocomplete="off" class="form" enctype="multipart/form-data" id="this-form" method="post">
                <fieldset>
                    <legend class="text-center">Diga-nos sobre você</legend>
                    {% csrf_token %}
                    {% bootstrap_messages %}
                    <div class="row">
                        <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma mb-2">
                            {% bootstrap_form model_form %}
                            {% buttons %}
                                <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
                            {% endbuttons %}
                        </div>
                    </div>
                </fieldset>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"interview-styles.css"
def css():
    """
    body {background-color: #3b5998;}
    .ma {margin: auto;}
    """

# todo Formulário class based view (FormView)
"InterviewFormView"
def views2():
    """
    from django.views.generic import FormView
    from django.urls import reverse_lazy

    class InterviewFormView(FormView):
        form_class = InterviewModelForm
        success_url = reverse_lazy('index')
        template_name = 'interview2.html'

        def form_valid(self, form, *args, **kwargs):
            form.save()
            messages.success(self.request, 'Formulário preenchido com sucesso. Obrigado por participar!')
            return super(InterviewFormView, self).form_valid(form, *args, **kwargs)

        def form_invalid(self, form, *args, **kwargs):
            messages.error(self.request, 'Houve algum erro em um ou mais dos campos do formulário')
            return super(InterviewFormView, self).form_invalid(form, *args, **kwargs)
    """

def pa_urls2():
    """
    from .views import InterviewFormView
    urlpatterns = [path('interview2/', InterviewFormView.as_view(), name='interview2')]
    """

"interview2.html"
def templates4():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/interview2-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Formulário 2 de entrevista</title>
    </head>
    <body>
        {% include 'fixed-return-button.html' %}
        <div class="container">
            <form autocomplete="off" class="form" enctype="multipart/form-data" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <fieldset><legend class="text-center">Diga-nos sobre você</legend></fieldset>
                <div class="row">
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma mb-2">
                        {% bootstrap_form form %}
                        {% buttons %}
                            <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
                        {% endbuttons %}
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"interview2-styles.css"
def css2():
    """
    body {background-color: #f46f30;}
    .ma {margin: auto;}
    """

# todo Formulário function based view (html puro)
"interview2"
def views3():
    """
    from .models import Interview
    from django.contrib import messages
    from django.shortcuts import redirect
    from django.shortcuts import render

    def interview2(request):
        if str(request.method) == 'POST':
            if request.POST.get('full_name') \
             and request.POST.get('email') \
             and request.POST.get('age') \
             and request.POST.get('gender') \
             and request.POST.get('nationality') \
             and request.POST.get('brief_description') \
             and request.POST.get('self_grade') \
             and request.POST.get('passtimes') \
             and request.FILES.get('avatar') != '':
                var = Interview(
                    full_name=request.POST.get('full_name'),
                    email=request.POST.get('email'),
                    age=request.POST.get('age'),
                    gender=request.POST.get('gender'),
                    nationality=request.POST.get('nationality'),
                    brief_description=request.POST.get('brief_description'),
                    self_grade=request.POST.get('self_grade'),
                    passtimes=request.POST.get('passtimes'),
                    avatar=request.FILES.get('avatar')
                )
                var.save()
                messages.success(request, 'Formulário preenchido com sucesso. Obrigado por participar!')
                return redirect('index')
            else:
                messages.error(request, 'Houve algum erro em um ou mais dos campos do formulário')

        return render(request, 'interview3.html')
    """

def pa_urls3():
    """
    from .views import interview2
    urlpatterns = [path('interview3/', interview2, name='interview3')]
    """

"form-fields.html"
def templates5():
    """
    <div class="row mt-2">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="full_name">Campo para escrever seu nome completo</label>
            <input type="text" class="form-control" id="full_name" name="full_name" min="2" max="200" placeholder="seu nome completo" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="email">Campo para escrever seu email</label>
            <input type="email" class="form-control" id="email" name="email" min="2" max="200" placeholder="seu email" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="age">Campo para escrever idade</label>
            <input type="number" class="form-control" id="age" name="age" min="1" max="120" placeholder="sua idade" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="exampleFormControlSelect1">Campo para selecionar um gênero</label>
            <label>Escolha um gênero</label>
            <select class="form-control" id="exampleFormControlSelect1" name="gender">
                <option>escolher...</option>
                <option>feminino</option>
                <option>masculino</option>
                <option>outro</option>
            </select>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="nationality">Campo para escrever nacionalidade</label>
            <input type="text" class="form-control" id="nationality" name="nationality" min="1" max="120" placeholder="sua nacionalidade" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2 col-7 col-sm-7 col-md-7 col-lg-7 col-xl-7">
            <label class="sr-only" for="brief_description">Campo para falar algo sobre você</label>
            <textarea class="form-control" id="brief_description" name="brief_description" placeholder="Fale algo sobre você" rows="7" cols="40" required></textarea>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="self_grade">Campo para dar a você uma nota</label>
            <input type="number" step="0.01" class="form-control" id="self_grade" name="self_grade" min="1" max="10" placeholder="sua nota auto-avaliativa" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="passtimes">Campo para escrever nacionalidade</label>
            <input type="text" class="form-control" id="passtimes" name="passtimes" min="1" placeholder="passatempo favorito" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="avatar">Campo para fazer upload do seu avatar</label>
            <label>Forneça seu avatar</label>
            <input type="file" class="form-control-file" id="avatar" name="avatar">
        </div>
    </div>
    """

"interview3.html"
def templates6():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/interview3-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Formulário 3 de entrevista</title>
    </head>
    <body>
        {% include 'fixed-return-button.html' %}
        <div class="container">
            <form autocomplete="off" class="form" enctype="multipart/form-data" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <fieldset><legend class="text-center">Diga-nos sobre você</legend></fieldset>
                <div class="row">
                    <div class="col-7 col-sm-7 col-md-7 col-lg-7 col-xl-7 ma mb-2">
                        {% include 'form_fields.html' %}
                    </div>
                </div>
                <div class="container text-center mb-5">
                    <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"interview3-styles.css"
def css3():
    """
    body {background-color: #ffdc7d;}
    .ma {margin: auto;}
    """

# todo Formulário class based view (CreateView)
"InterviewCreateView"
def views4():
    """
    from django.contrib.messages.views import SuccessMessageMixin
    from django.urls import reverse_lazy
    from django.views.generic import CreateView
    from .models import Interview

    class InterviewCreateView(SuccessMessageMixin, CreateView):
        fields = ('full_name', 'email', 'age', 'gender', 'nationality',
                  'brief_description', 'self_grade', 'passtimes', 'avatar')
        model = Interview
        success_message = 'Formulário preenchido com sucesso. Obrigado por participar!'
        success_url = reverse_lazy('index')
        template_name = 'interview4.html'
    """

def pa_urls4():
    """
    from .views import InterviewFormView
    urlpatterns = [path('interview4/', InterviewCreateView.as_view(), name='interview4')]
    """

"form-fields.html"
def templates7():
    """
    <div class="row mt-2">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="full_name">Campo para escrever seu nome completo</label>
            <input type="text" class="form-control" id="full_name" name="full_name" min="2" max="200" placeholder="seu nome completo" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="email">Campo para escrever seu email</label>
            <input type="email" class="form-control" id="email" name="email" min="2" max="200" placeholder="seu email" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="age">Campo para escrever idade</label>
            <input type="number" class="form-control" id="age" name="age" min="1" max="120" placeholder="sua idade" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="exampleFormControlSelect1">Campo para selecionar um gênero</label>
            <label>Escolha um gênero</label>
            <select class="form-control" id="exampleFormControlSelect1" name="gender">
                <option>escolher...</option>
                <option>feminino</option>
                <option>masculino</option>
                <option>outro</option>
            </select>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="nationality">Campo para escrever nacionalidade</label>
            <input type="text" class="form-control" id="nationality" name="nationality" min="1" max="120" placeholder="sua nacionalidade" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2 col-7 col-sm-7 col-md-7 col-lg-7 col-xl-7">
            <label class="sr-only" for="brief_description">Campo para falar algo sobre você</label>
            <textarea class="form-control" id="brief_description" name="brief_description" placeholder="Fale algo sobre você" rows="7" cols="40" required></textarea>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="self_grade">Campo para dar a você uma nota</label>
            <input type="number" step="0.01" class="form-control" id="self_grade" name="self_grade" min="1" max="10" placeholder="sua nota auto-avaliativa" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="passtimes">Campo para escrever nacionalidade</label>
            <input type="text" class="form-control" id="passtimes" name="passtimes" min="1" placeholder="passatempo favorito" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="avatar">Campo para fazer upload do seu avatar</label>
            <label>Forneça seu avatar</label>
            <input type="file" class="form-control-file" id="avatar" name="avatar">
        </div>
    </div>
    """

"interview4.html"  # Por ser uma CreateView, não recomenda-se ter o atributo [ action="" ]
def templates8():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/interview4-styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Formulário 4 de entrevista</title>
    </head>
    <body>
        {% include 'fixed-return-button.html' %}
        <div class="container">
            <form autocomplete="off" enctype="multipart/form-data" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <fieldset><legend class="text-center">Diga-nos sobre você</legend></fieldset>
                <div class="row">
                    <div class="form-group ma">
                        <div class="col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 ma">
                            {% include 'form_fields.html' %}
                            <div class="container text-center mb-5">
                                <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

"interview4-styles.css"
def css4():
    """
    body {background-color: #292929; color: silver;}
    .ma {margin: auto;}
    """
