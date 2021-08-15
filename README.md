[![build](https://github.com/ajthr/flask-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/ajthr/flask-boilerplate/actions/workflows/ci.yml)

flask-boilerplate
=================

Flask Restful API Boilerplate

what does flask-boilerplate include
-----------------------------------

-   Custom commands for ease of use
    -   make - Adds a migrations folder to the application.
    -   migrate - Generates and Applies migration to the database after database is ready to accept connections.
    -   test - Run tests for the application.
    -   create-app - Create an app with a predefined structure.
    -   deploy - Run app with gunicorn
-   Mysql for DB
    -   Mysql is configured and ready to be used.
-   Project structure
    -   Related files can be grouped.
    -   Components can be isolated.
-   Dockerized

### Running the project

with docker
-----------

-   create a .env file in the working directory and add environment variables.
    ```
    DB_ADMIN_USER=<user> 
    DB_ADMIN_PWD=<userpwd>
    DB_ROOT_PWD=<rootpwd>
    ```

-   Build services:
    ```docker-compose build```

-   Run the project:
    ```docker-compose up```

without docker
--------------

-   make sure MySQL is installed in the system.
-   only the app folder is required to run the project without docker.
    you may delete the rest.
-   create a .env file in the app directory and add environment variables
    ```
    DATABASE_HOST=<host>
    DATABASE_NAME=<name>
    TEST_DATABASE_NAME=<test_db name>
    DATABASE_PORT=<port>
    DATABASE_USER=<user>
    DATABASE_PASSWORD=userpwd
    ```

-   clone the repo and go to the project's directory.
-   install the dependencies:
    `pip install -r requirements.txt`

-   create the migrations folder
    `flask make`

-   generate and apply the migrations. (run this command when you make changes in the database models)
    `flask migrate`

-   Run the project:
    `flask run`

### Testing

-   with docker:
    `docker exec -it app sh -c "flask test"`

-   without docker:
    `flask test`

Copyright (c) 2021 Ajith Ramachandran

[MIT License](LICENSE)
