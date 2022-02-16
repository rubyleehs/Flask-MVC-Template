from flask import Flask, render_template
from flask_migrate import Migrate
from models.Todo import db
from routes.todo_bp import todo_bp


app = Flask(__name__)
app.config.from_object('config')
app.app_context().push()

# Will need to create a db is one does not exist
# Can make empty one wit
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(todo_bp, url_prefix='/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
    # print(app.url_map)