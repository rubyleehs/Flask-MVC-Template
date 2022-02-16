from flask import render_template, redirect, url_for, request, abort
from models.Todo import Todo
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

def delete(id):
    task = db.session.merge(Todo.query.get_or_404(id))
    db.session.delete(task)
    db.session.commit()
    try: 
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your task'

def update(id):
    task = db.session.merge(Todo.query.get_or_404(id))

    if(request.method == 'POST'):
        task.content = request.form['content']
        try: 
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating that task"
    else:
        return render_template('update.html', task=task) 