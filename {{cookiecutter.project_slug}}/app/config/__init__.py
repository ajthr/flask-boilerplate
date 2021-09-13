import os
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from config import settings, utils

app = Flask(__name__)

# app config
app.config["DEBUG"] = settings.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


@app.cli.command("make")
def flask_make():
    """Creates a new migration repository."""
    # flask db init performs the same task. But raises error if the folder is already present.
    if os.path.isdir("migrations"):
        click.echo("migrations folder already exist. skipping...")
    else:
        os.system("flask db init")


@app.cli.command("migrate")
def flask_migrate():
    """Autogenerate a new revision file and Upgrade to a later version."""
    utils.wait_for_db(db)
    if os.path.isdir("migrations"):
        os.system("flask db migrate")
        os.system("flask db upgrade")
    else:
        click.echo("Error: Path doesn't exist: '{}/migrations'. Please use the 'make' command to create a new scripts folder.".format(os.getcwd()))


@app.cli.command("test")
def flask_test():
    """Run tests for all apps."""
    utils.wait_for_db(db)
    os.system("python -m unittest discover")


@app.cli.command("create-app")
@click.argument("app")
def flask_create_app(app):
    file_tree = [
        {
            "filename": "/__init__.py",
            "permission": "x",
            "content": ""
        },
        {
            "filename": "/models.py",
            "permission": "w+",
            "content": "from config import db\n\n# create your models here"
        },
        {
            "filename": "/routes.py",
            "permission": "w+",
            "content": "from flask import Blueprint\n\n{}_blueprint = Blueprint('{}', __name__)\n\n# create your routes here.".format(app, app)
        },
        {
            "filename": "/schema.py",
            "permission": "w+",
            "content": "from flask_marshmallow import Schema\n\n# create your schema here"
        },
    ]
    if os.path.isdir(app):
        click.echo(
            "Error: Directory exist: {}/{} already exists.".format(os.getcwd(), app), err=True)
    else:
        basedir = '/'.join([os.getcwd(), app])
        os.mkdir(basedir)
        for file in file_tree:
            f = open(basedir + file.get("filename"), file.get("permission"))
            if file.get("content") != "":
                f.write(file.get("content"))
            f.close()


@app.cli.command("deploy")
@click.option("-h", "--host", "host", default="0.0.0.0")
@click.option("-p", "--port", "port", default=5000)
@click.option("-w", "--workers", "workers", default=1)
@click.option("-k", "--worker-class", "worker_class", default="sync")
@click.option("-n", "--name", "app_name")
@click.option("-c", "--config", "config")
def flask_deploy(host, port, workers, worker_class, app_name, config):
    if config is not None:
        os.system("gunicorn -w {} -b {}:{} -k {} -n {} -c {} app:app".format(workers,
                  host, port, worker_class, app_name, config))
    else:
        os.system("gunicorn -w {} -b {}:{} -k {} -n {} app:app".format(workers,
                  host, port, worker_class, app_name))
