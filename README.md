# wsBackend-Fabrica25.2
Sistema de manutenção de usuários (CRUD) e utilização de uma API externa (https://ip-api.com/docs/api:json).

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
-- Obs: Para parar de executar, no terminal clique "Crtl + c"


# Integrando uma API ao projeto
Importar o requests e o HttpResponse

import requests
from django.http import HttpResponse


## Integrando com o MySQL
Ao baixar o MySQL é bom coloca-lo no Path, para executar os comandos.

No MySQL workbench
Execute:
```bash
  CREATE DATABASE IF NOT EXISTS djangoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
Foi criado o banco.

No VSCode
Terminal:
```bash
  pip install mysqlclient
```
No config/settings.py, altere o modo de conexão com o DB.

```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoDB',  
        'USER': 'root',            
        'PASSWORD': 'sua_senha',  
        'HOST': '127.0.0.1',   
        'PORT': '3306',          
    }
}
```
# Para fazer o teste de conexão. 

No Power Shell
- vereifique estar no diretorio correto (seu projeto e com o venv ativado)
.\venv\Scripts\activate

```bash
 python manage.py dbshell
 ```
Ao executar este comando ele entratará no diretório do MySQL. Execute
```bash
    SELECT DATABASE();
 ```
```bash
    SHOW TABLES;
 ```

Verificando os dados na tabela. (Power Shell ou mysql workbench)
**mysql workbench** - rode o USE djangoDB;
 ```bash
    USE djangoDB;
 ```
 ```bash
    SELECT * FROM app_aluno;
 ```
 ```bash
    SELECT * FROM app_professor;
 ```

Sair no PowerShell
exit;
- Volta no diretorio do projeto, execute
```bash
 python manage.py dbshell
 ```