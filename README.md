# a-CRUDe-flask-tutorial
Walk-through to write a super simple CRUD API in python using flask.

## Prerequisites and Scope
This tutorial assumes a basic understanding of Python, and to an extent SQL.

It is also assumed that you have Python and pip installed on your system.

## Contents
- [Getting Started](#getting-started)

## Getting Started

### Project Structure
```sh
-demo/
|-env/ *generate with virtualenv*
|-templates/ *contains html file templates*
||-index.html
|-static/ *static files to be served*
||-style.css
||-index.js
|-app.py
|-database.db
```

### Setting up virtualenv (optional)
```sh
pip install virtualenv
```

```sh
virtualenv env
```
#### 'Activating' virtualenv
```sh
source ./env/bin/activate
```
### Installing Flask
```sh
pip install flask
```

### Initialize Database
```sh
sqlite3 database.db
```
```sh
sqlite> create table student(rollno integer primary key, name text, grade text);
```
