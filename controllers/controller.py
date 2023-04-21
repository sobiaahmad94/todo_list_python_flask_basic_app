from app import app
# from app.py, import the variable app
from flask import render_template
from models.todo_list import tasks

@app.route('/tasks') # request is here, looks at view finder a
# @app.route('/')
# def index():
#   return "Go me, im awesome!!!"
def index():
    return render_template('index.jinja', title = 'Home', tasks = tasks)
    # return "Go me - dinosaursssssss" # response sending back to client

# decorator is wrapped around a function
# the result of the function would run 

# @app.route('/<name>')
# def greet(name):
#     return f"Hello {name}!"