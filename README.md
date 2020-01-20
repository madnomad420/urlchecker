# Mail checker

## Requirements

* Python
* MySQL/MariaDB

## Prepare
Create MySQL database

## Installation
```
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuser 
```
and follow instructions

## Run

Run server
```
$ MYSQL_DATABASE={database_name} MYSQL_USER={database_user} MYSQL_PASSWORD={database_password} MYSQL_HOSTNAME={database_host} MYSQL_PORT={database_port} ./manage.py runserver
```
eg.
```
$ MYSQL_DATABASE=urlchecker MYSQL_USER=root MYSQL_PASSWORD=root MYSQL_HOSTNAME=localhost MYSQL_PORT=3306 ./manage.py runserver
```

## Use

Open http://localhost:8000/

