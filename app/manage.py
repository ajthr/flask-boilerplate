#!usr/bin/env python

import os
import sys

def execute_from_command_line(args):
    if len(args) > 2:
        raise RuntimeError(
            "ambiguous arguments. please specify one argument."
        )
    elif args[1] == "init":
        if os.path.isdir("migrations"):
            print("migrations folder already exist. skipping...")
        else:
            os.system("flask db init")
    elif args[1] == "migrate":
        os.system("flask db migrate")
    elif args[1] == "upgrade":
        os.system("flask db upgrade")
    elif args[1] == "runserver":
        os.system("python app.py")
    elif args[1] == "test":
        os.system("python -m unittest discover")
    elif args[1] == "--help":
        print("\tFlask Boilerplate Help\n\n\
        init        - Adds a migrations folder to the application.\n\
        migrate     - Generates an initial migration.\n\
        upgrade     - Applies the migration to the database.\n\
        runserver   - Start the application server.\n\
        test        - Run tests for the application.\n")
    else:
        raise RuntimeError(
            "Couldn't find the command you just entered."
            "use --help to view available commands."
        )

def main():
    # check if all required packages are installed and can be imported
    # try:
    #     import flask
    #     import flask_migrate
    #     import flask_sqlalchemy
    #     import marshmallow
    # except ImportError as exception:
    #     raise ImportError(
    #         "Couldn't import required packages."
    #         "please install packages from requirements file."
    #     ) from exception
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
