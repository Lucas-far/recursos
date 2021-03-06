

# Criam-se os módulos essenciais para realizar o deploy
def raiz():
    """
    1. raiz / botão direito / new / file / .gitignore  -> inserir -> __pycache__ *.*~ *.pyc .idea  # '\n' para cada
    2. raiz / botão direito / new / file / Procfile    -> inserir -> web: gunicorn pp.wsgi --log-file -
    3. raiz / botão direito / new / file / runtime.txt -> inserir -> python-retorno do comando python -V no terminal
    """

# Instalar dependências essenciais
def terminal():
    """ pip install gunicorn whitenoise """

# Registrar uma das dependências, no índice 1
def settings():
    """
    DEBUG = False
    MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
    """

# Comandos de coletagem e inspeção
def terminal2():
    """
    1. python manage.py collectstatic   # copiar módulos do modo desenvolvimento para o modo produção
    2. pip freeze > requirements.txt    # congelar bibliotecas
    3. pip install -r requirements.txt  # verificar se todas as bibliotecas estão corretamente instaladas
    """

# Comandos relacionados ao GitHub
def terminal3():
    """
    1. git config --global user.email "seu_email"
    2. git config --global user.name "seu_nome"
    3. git init                # Iniciar o git atrelado ao seu projeto python com django
    4. git status              # Verificar se há modulos a serem enviados via commit
    5. git add .               # Adicionar módulos não registrados, via commit
    6. git commit -m "config"  # Criar módulo para commit (às vezes é preciso repetir, caso haja demora)
    7. git status              # Verificar se todos os módulos foram, de fato, exportados, via commit
    """
    # Caso seja um primeiro acesso, os comandos 1 e 2 precisem ser usados

# Comandos Heroku, onde o 3 gera links que devem ser copiados
def terminal4():
    """
    1. heroku login                                                # Logar no Heroku de dentro do projeto
    2. heroku create av-sufixo desejado --buildpack heroku/python  # Criar um rota para a aplicação do projeto
    3. git push heroku master                                      # Criar a aplicação
    """

# Adicionar a rota criada no deploy, para configurar a rota do modo produção
def settings2():
    """
    ALLOWED_HOSTS = ['link da aplicação sem o https:// e sem / ao final']
    """

# Repetir comandos Git
def terminal5():
    """
    1. git init
    2. git status
    3. git add .
    4. git commit -m "config2"
    5. git status
    6. git push heroku master
    7. heroku logs --tail
    """

# Comandos Heroku relevantes
def terminal6():
    """
    1. heroku pg:reset DATABASE_URL
    2. heroku run python manage.py migrate
    3. heroku run python manage.py createsuperuser
    """
    # 1 serve para resetar todos os bdds criados na app Django
