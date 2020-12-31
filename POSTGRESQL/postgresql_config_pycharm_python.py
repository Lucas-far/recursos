

"""
Objetivo:
         configurar um bdd postgreSQL dentro de um projeto Django
"""

def pgadmin4():
    """
    1. Abrir o software Pgadmin4
    2. Logar no usuário não root [ não postgres ]

    3. Pós login:
       Databases
           botão direito
               create
                   database
                       name = nome criado terá de ser passado no módulo [ settings.py / DATABASES / NAME ]
                           save
    """

def terminal():
    """
    1. pip install psycopg2-binary
    2. pip freeze > requirements.txt
    """

def settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nome do bdd no PgAdmin4',
            'USER': 'lu**a***n',
            'PASSWORD': 'pa*****t27**',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    """

def deploy_heroku():
    """
    1. pip install dj-database-url
    2. pip freeze > requirements.txt
    3. import dj_database_url
    4. Comentar DATABASES
    5. DATABASES = {'default': dj_database_url.config()}
    6. git init
    7. git status
    8. git add .
    9. git commit -m "deploy_initial_config" (repetir, caso demore demais...)
    10. git status
    11. heroku login
    12. heroku create av.sufixo desejado --buildpack heroku/python
    13. git push heroku master
    14. heroku run python manage.py migrate
    15. heroku run python manage.py createsuperuser
    """
