# GreenCart

[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## Prerequisites
- Python
- Git


## Installation 

```bash
$ git clone https://github.com/YashSahsani/GreenCart.git && cd GreenCart
```

### Install Virtual Env

```bash
$ pip install virtualenv
$ virtualenv venv
```

### OR

```bash
$ python3 -m venv venv # create virtual enviroment
```

### For Mac/ Linux

```bash
$ source venv/bin/activate # activate virtual env for Mac and Linux
$ pip install -r requirements.txt
```

### For Windows

```bash
$ .\venv\bin\activate # activate virtual env for Windows
$ .\venv\Scripts\activate
$  pip install -r requirements.txt
```

### Migrations

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### For Adding initial data
```bash
$ python manage.py loaddata data.json

Admin-Email:- admin@greencart.com
Admin-Password:- Admin@123

TestUser-Email:- test@greencart.com
TestUser-Password:- Test@123
```