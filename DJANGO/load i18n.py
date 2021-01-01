

"""
Módulo >>> load i18n.py
"""
# TODO -> Configurar {% load i18n %}

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 8:Trabalhando com tradução de projetos
    Aula:   # 76. Traduzindo no template
    """

def terminal():
    """
    1. pip install django==2.2.9
    2. pip install django-bootstrap4
    3. pip freeze > requirements.txt
    4. django-admin startproject pp .
    5. django-admin startapp pa
    """

# Na var MIDDLEWARE, recomenda-se inserir a string do middleware no índice 1
def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    MIDDLEWARE = ['django.middleware.locale.LocaleMiddleware']
    TEMPLATES = [{'DIRS': ['templates']}]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    LOCALE_PATHS = ((os.path.join(BASE_DIR, 'locale'),))
    """

def raiz():
    """ raiz/new/directory/locale """

"OBS: No módulo views, a tradução ocorre em variáveis string passadas em contexto, envoltas ao método _()"

# IndexTemplateView / index.html
def views():
    """
    from django.contrib import messages
    from django.views.generic import TemplateView
    from django.utils.translation import gettext as _

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super(IndexTemplateView, self).get_context_data(**kwargs)
            context['how_are_you'] = _('Como você está?')
            return context
    """

# function_based_view / fbv.html
def views2():
    """
    from django.shortcuts import render
    from django.utils.translation import gettext as _

    def function_based_view(request):
        context = {'welcome': _('Seja bem-vindo à página Índice')}
        return render(request, 'fbv.html', context)
    """

# StandardFormView / form.html
def views3():
    """
    from django.contrib import messages
    from django.urls import reverse_lazy
    from django.views.generic import FormView
    from .forms import *

    class StandardFormView(FormView):
        template_name = 'form.html'
        form_class = StandardForm
        success_url = reverse_lazy('index')

        def form_valid(self, form, *args, **kwargs):
            form.print_data_into_terminal()
            messages.success(self.request, _('Sua mensagem foi enviada. Obrigado!'))
            return super(StandardFormView, self).form_valid(form, *args, **kwargs)

        def form_invalid(self, form, *args, **kwargs):
            messages.error(self.request, _('Há algum erro no seu formulário!'))
            return super(StandardFormView, self).form_invalid(form, *args, **kwargs)
    """

# TODO -> Configuração aparte ================================================================================== INÍCIO

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('fbv/', function_based_view, name='fbv/'),
        path('form/', StandardFormView.as_view(), name='form/')
    ]
    """

# TODO -> Configuração aparte ===================================================================================== FIM

"OBS: No template, textos em tag são traduzidos pela sintaxe {% trans '' %}"
"OBS: No template, variáveis de contexto são traduzidas, caso tenham sido _() dentro da view"
"OBS: Não deve-se esquecer também de usar a sintaxe {% load i18n %}"
"OBS: Os módulos editáveis principais: [ forms ] [ models ] [ templates ] [ views ]"

# index.html
def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load i18n %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        {% bootstrap_messages %}
        <h2>{% trans "Seja bem-vindo à página Índice" %}</h2>
        <hr>
        <label for="questions">{{ how_are_you }}</label>
        <div>
            <select id="questions" size="7" multiple>
                <option value="answer1">{% trans "Uma droga!" %}</option>
                <option value="answer2">{% trans "Tudo bem!" %}</option>
                <option value="answer3">{% trans "Uma maravilha!" %}</option>
                <option value="answer4">{% trans "Não sei dizer!" %}</option>
            </select>
        </div>
    </body>
    {% bootstrap_javascript jquery='full' %}
    </html>
    """

# fbv.html
def templates2():
    """
    <!DOCTYPE html>
    {% load i18n %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h2>{{ welcome }}</h2>
        <hr>
        <label for="questions">{% trans "Qual dessas frases é mentira?" %}</label>
        <div>
            <select id="questions" size="7" multiple>
                <option value="cat">{% trans "Gatos gostam muito de banhar" %}</option>
                <option value="dog">{% trans "Cachorros são grandes companheiros" %}</option>
                <option value="pig">{% trans "Porcos são normalmente rosados" %}</option>
                <option value="grasshopper">{% trans "Gafanhotos voam" %}</option>
            </select>
        </div>
    </body>
    </html>
    """

# form.html
def templates3():
    """
    <!DOCTYPE html>
    <html lang="en">
    {% load i18n %}
    {% load bootstrap4 %}
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h2>{% trans "Formulário" %}</h2>
        <hr>
        <form action="{% url 'form/' %}" id="this-form" method="post">
            {% csrf_token %}
            {% bootstrap_messages %}
            <input min="2" max="150" name="email" size="40" placeholder="{% trans 'seu e-mail' %}" type="email">
            <input min="2" max="150" name="question" size="40" placeholder="{% trans 'sua pergunta' %}" type="text">
            <button form="this-form" type="submit">{% trans "Enviar" %}</button>
        </form>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# Traduções podem ser feitas no primeiro parâmetro da criação de um campo: label='' / strings usadas em def form
def forms():
    """
    from django import forms
    from django.utils.translation import gettext as _
    from django.core.mail.message import EmailMessage

    class StandardForm(forms.Form):
        email = forms.CharField(label=_('Seu email'), min_length=2, max_length=150)
        question = forms.CharField(label=_('Faça sua pergunta'))

        def print_data_into_terminal(self):
            content = \
                f'''
                ===== {_('Impressão de dados')} =====
                {_('Email')}: {self.cleaned_data['email']}
                {_('Pergunta')}: {self.cleaned_data['question']}
                '''

            data_printer = EmailMessage(
                body=content,
                headers={'Reply-To': self.cleaned_data['email']},
                subject=_('Opinião do usuário'),
                to=('meu_email@domínio.com',),
                from_email='meu_email@domínio.com'
            )
            data_printer.send()
    """

# Traduções podem ser feitas em: parâmetro 1 de campo / var choices / var verbose
def models():
    """
    from django.db import models
    from django.utils.translation import gettext as _

    class RandomModel(models.Model):
        choices_gender = (
            ('feminino', _('feminino')),
            ('masculino', _('masculino')),
            ('outro', _('outro'))
        )
        animal = models.CharField(_('Animal favorito'), max_length=100)
        gender = models.CharField(_('Gênero'), choices=choices_gender, max_length=9)

        class Meta:
            verbose_name = _('Animal')
            verbose_name_plural = _('Animais')
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(RandomModel)
    class RandomModelAdmin(admin.ModelAdmin):
        list_display = ('animal', 'gender')
    """

def terminal2():
    """
    1. python manage.py makemessages -l
    2. Após o [ -l ] insere-se o símbolo da língua que você deseja criar um módulo de tradução
        EXEMPLO: python manage.py makemessages -l en
    3. http://www.i18nguy.com/unicode/language-identifiers.html
    4. Ao executar, conteúdos envoltos por _() e {% trans '' %}, serão coletados e enviados ao diretório: [ locale ]
    5. A tradução costuma ser feita manualmente, mas há softwares pagos que podem ajudar

    #1. criar o diretório e módulos para poder traduzir
    #3. listagem de códigos das línguas
    """

def locale():
    """
    1. locale/lang/LC_MESSAGES/django.po  # É o módulo onde traduções são feitas
    2. não esquecer de salvar as alterações antes dos próximos passos [ ctrl + s ]
    """

def terminal3():
    """
    1. python manage.py compilemessages  # compilar mensagens traduzidas
    2. python manage.py migrate
    3. python manage.py createsuperuser  # para analisar se os conteúdos admin foram traduzidos
    4. python manage.py runserver
    """

def browser():
    """
    1. É preciso testar se as traduções foram compiladas com êxito
    2. Para vizualizar se a tradução teve êxito, é preciso mudar a preferência de linguagem no navegador

    OBS:
        1. Não foi explicado no curso, como fazer um dropdown, para escolher a língua de forma prática no template
        2. É recomendável pesquisar sobre isso
    """
