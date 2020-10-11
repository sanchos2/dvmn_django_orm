# Description

This is a learning project from [devman](https://dvmn.org/modules/django-orm/) (lesson 1)

## How to setup

Install python3

```sh
sudo apt install python3
sudo apt install python3-pip
```

Download the project and install dependencies

```sh
git clone https://github.com/sanchos2/dvmn_django_orm.git
cd dvmn-django-orm
pip3 install -r requirements.txt
```

Add environment variables:

```
DB_HOST=database server address
DB_PORT=database server port
DB_NAME=database name
DB_USER=database user
DB_PASSWORD=database password
SECRET_KEY=secret key
DEBUG=True
```
note: on production environment setup DEBUG to False

## How to run

Run project

```sh
python3 main.py
```

GOTO http://127.0.0.1:8000