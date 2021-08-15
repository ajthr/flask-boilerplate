[![build](https://github.com/ajthr/flask-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/ajthr/flask-boilerplate/actions/workflows/ci.yml)   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  ![version](https://img.shields.io/badge/version-0.1-orange)

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
-   export environment variables
    ```
    $ export DATABASE_HOST=<host>
    $ export DATABASE_NAME=<name>
    $ export TEST_DATABASE_NAME=<test_db_name>
    $ export DATABASE_PORT=<port>
    $ export DATABASE_USER=<user>
    $ export DATABASE_PASSWORD=userpwd
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
