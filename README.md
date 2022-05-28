## Setting up Django Backend
Open a new terminal window and run the following command to create a new project directory:
```sh
mkdir api-django
```
Navigate inside the directory
```sh
cd api-django
```
Good practice is for each new project to using isolated virtual environment lik "venv".
**venv** is the standard tool for creating virtual environments, and has been part of Python since Python 3.3

Generate new venv with command:
```sh
python3 -m venv .venv
```
Now we need to activate venv:
```sh
source .venv/bin/activate

# on success prompt will look like this:
(venv)$: 
```
Now is time to install needed python packages with pip3
```sh
pip3 install django
```


Django have handy command that will generate new project for us:
```
django-admin startproject backend
```

This directory is root for our Project. Each Django project cant hav multiple application inside this directory.

![](./screenshots/django-project-and-applications-example.png)

navigate into the newly created backend dir
```sh
cd backend
```

Start a new application called todo(inside venv it doesn't mether if commands are with  python or python3):
```sh
python manage.py startapp todo
or
python3 manage.py startapp todo
```
now we have dir for our first Application:
![](./screenshots/startapp-todo.png)

Django have another handy command that will generate new Database for us:
```sh
python manage.py migrate
```
In terminal we will see:
```sh
python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
This command will create file "db.sqlite3" this is out database

Now is time to run and see our new backend website:
```sh
python manage.py runserver
```
Output in terminal will be:
```sh
python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 28, 2022 - 19:10:43
Django version 4.0.4, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
click over URL:[http://127.0.0.1:8000/](http://127.0.0.1:8000/)  or just open it in browser

![](./screenshots/django-runserver.png)

If all is OK you can stop the server with keys combination CTRL+C.

Because it's god practice each project to be track witt git version control we need to create new file with name ".gitignore" in our root directory "api-django":

```sh
# Environments 
.venv 

# Django #
*.log
*.pot
*.pyc
__pycache__
```
This will reduce cont of file in our github repo and will make our project more reusable.
Notice files and folders with grey color, this mean that they are not included anymore in git version control.
![](./screenshots/gitignore-creating.png)



Now is time to continue work over our fist Django application
Open file "backend/settings.py" and find section "Application definition" and add new finale line like this

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo' # our first Django Application
]
```
Save change to file.