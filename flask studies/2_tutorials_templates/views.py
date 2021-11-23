from flask import render_template

def index():
    return 'Welcome to Home Page'

def index_tem(name, marks):
    # for default it will search in templates folder
    return render_template('index.html', name=name, marks=marks)

def index_tem_for():
    items = {'Python': 20, 'Jinja': 80, 'Flask':50}
    # for default it will search in templates folder
    return render_template('index_for.html', data=items)
