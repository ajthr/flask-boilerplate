from flask import Flask

from config import settings
from config import db, migrate

from users.routes import users_blueprint

import os

app = Flask(__name__)

# app config
app.config["DEBUG"] = settings.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

# initialize db
db.init_app(app)
migrate.init_app(app, db)

# register blueprints
app.register_blueprint(users_blueprint, url_prefix='/users')

@app.route('/')
def hello_world():
    return 'Hello from flask boilerplate'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host="0.0.0.0")
