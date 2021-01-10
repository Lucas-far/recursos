

"""
Módulo >>> template_view.py

Objetivo:
         exemplificar o funcionamento da cbv TemplateView

Palavra chave >>> configurar template view
"""

def quando_usar():
    """
    1 - Quando quer-se mostrar somente dados comuns, como links, textos, dados normais/consolidados
    2 - Sendo assim, é melhor evitar TemplateView para passar objetos de modelos que alteram-se, formulários
    """

"OBS"  # não será feito um projeto para exemplificar, apenas o esqueleto padrão
"OBS"  # Esse tipo de cbv permite chamar métodos, como [ def get_context_data ]
"OBS"  # Contextos são comuns para chamar: modelos e seus objetos, strings, bibliotecas
def views():
    """
    from django.views.generic import TemplateView
    from .models import Modelo

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super(IndexTemplateView, self).get_context_data(**kwargs)
            context['modelo'] = Modelo.objects.order_by('?').all()
            context['texto'] = 'Texto qualquer'
            return context
    """
