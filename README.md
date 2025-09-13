# wsBackend-Fabrica25.2
Sistema de manutenção de usuários (CRUD) e utilização de uma API externa (https://ip-api.com/).

## Inicializando o Django

Instalar o Django:

```bash
  pip install django
```
Criar um projeto (será gerado um folder com o nome escolhido)

```bash
  django-admin startproject projeto .
```
Ativando o venv

```bash
  python -m venv venv
  venv\Scripts\activate
```
Criando o app(escolha de nome)

```bash
  python manage.py startapp randonName
```

Criar um file dentro do randonName/
- urls.py
- forms.py

No projeto/settings.py
```bash
- INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'randonName', #adicionar o randonName
] 
```

No /models.py criar a class
- Sempre que houver mudanças no models precisa realizar esses comandos.
```bash
  python manage.py makemigrations
  python manage.py migrate
```

Após tudo certo, de um run. Acessar pelo browser "localhost:8000" ou clicando no link que aparecera no terminal.

Rodar o Django
```bash
  python manage.py runserver
```
