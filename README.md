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
### Installing Flask, Flask-RESTful, Flask-SQLAlchemy and pymysql
```sh
pip install flask
pip install flask-restful
pip install flask-sqlalchemy
pip install pymysql
```

### Initialize Database
```sh
mysql -u <username> -p
```
```sh
mysql> create database test
mysql> connect test
```
```sh
mysql> create table student(rollno integer primary key, name text, grade text);
```

### Set Environment Variables and Run Flask
Set environment variables:
```sh
export FLASK_APP=app.py
export FLASK_DEBUG=true
```
Run flask:
```sh
flask run
```

## Displaying a Webpage
In ```demo/templates``` create a file ```index.html```. This will contain the skeliton of the webpage which we will serve, as well as the JavaScript needed to communicate with the API we will write.

```html
<html>
    <head>
        <title>Demo Title</title>
    </head>
    <body>
        <input type="text" name="name" id="name" placeholder="name" /><br>
        <input type="text" name="rollno" id="rollno" placeholder="rollno" /><br>
        <input type="text" name="grade" id="grade" placeholder="grade" /><br>
        <input type="button" name="submit" id="submit" value="submit" />
        <hr>
        <div id='student_info'></div>

        <script>
            // need to write JavaScript stuff here
        </script>
    </body>
</html>
```

Now we have to write our server in ```app.py``` to display the webpage.
First, lets import the necessary stuff
```python
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
```

Create instance of application and add configurations

```python
app = Flask(__name__)
```
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test' # this is the only one that is absolutly necessary, the rest just makes life much easier
app.config['SQLALCHEMY_ECHO'] = True # show error messages
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # reduce overhead
```

Now, to display ```index.html``` add:
```python
@app.route("/")
def show_entries():
    return render_template('index.html',error='')
```
Now go to ```http://localhost:5000/``` on your browser, and it should display your webpage.

## Database Stuff with SQLAlchemy

## API Stuff

