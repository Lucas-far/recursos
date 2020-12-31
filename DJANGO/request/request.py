

"""
Objetivo:
         exibir dados de usuário no template, ou para condições no módulo [ views.py ]
"""

def fonte():
    """
    Curso # Programação Web com Python e Django framework: Essencial
    Local # Seção 3:Django Framework Básico
    Aula  # 29. Usando e abusando do Django Shell
    """

def terminal():
    """
    python manage.py shell
    dir(request)
    """

def retorno():
    """
    ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
     '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
      '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
       '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding',
        '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files',
         '_mark_post_parse_error', '_messages', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body',
          'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding',
           'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie',
            'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline',
             'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']
    """

def views():
    """
    print(request)
    print(request.user)
    print(request.method)
    print(request.headers)

    for pk, item in enumerate(request.headers.items()):
        print(pk, item)

    COMANDOS PARA USUÁRIOS LOGADOS E COM CAMPOS ESPECIFICADOS PREENCHIDOS

        print(request.user.first_name)
        print(request.user.last_name)
        print(request.user.username)
        print(request.user.email)
        print(request.user.last_login)
        print(request.user.password)
    """
