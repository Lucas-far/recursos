

"""
Objetivo:
         Ordenar pk's desordenados

Observação:
           ao fazer isso, cópias dos objetos são criadas, então deleta-se os objetos com pk's desordenados
"""

def terminal():
    """
    python manage.py shell
    from pa.models import Modelo
    queryset = User.objects.all()
    lesser = int (objeto de menor pk)
    bigger = int (objeto de maior pk)
    value = int (valor pk inicial)

    while lesser < bigger:
        for obj in queryset:
            obj.pk = value
            obj.save()
            lesser += 1
            target += 1
    """
