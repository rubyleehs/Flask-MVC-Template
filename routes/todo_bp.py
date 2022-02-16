from flask import Blueprint
from controllers.TodoController import index, delete, update

todo_bp = Blueprint('todo_bp', __name__)
todo_bp.route('/', methods=['GET', 'POST'])(index)
todo_bp.route('/delete/<int:id>', methods=['GET'])(delete)
todo_bp.route('/update/<int:id>', methods=['GET', 'POST'])(update)
