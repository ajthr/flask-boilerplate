[![test](https://github.com/ajthr/flask-boilerplate/actions/workflows/test.yml/badge.svg)](https://github.com/ajthr/flask-boilerplate/actions/workflows/test.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![version](https://img.shields.io/badge/version-0.2-orange)

# flask-boilerplate

Flask Boilerplate for app and api

## Features

-   Custom commands for ease of use
    -   make - Adds a migrations folder to the application.
    -   migrate - Generates and Applies migration to the database after database is ready to accept connections.
    -   test - Run tests for the application.
    -   create-app - Create an app with a [predefined structure](docs/app_structure.md).
    -   deploy - Run app with gunicorn
-   Mysql for DB
    -   Mysql is configured and ready to be used.
-   Project structure
    -   Related files can be grouped.
    -   Components can be isolated.
-   Dockerized

## Quick Start

First, install cookiecutter if you don't already have it:

```bash
pip3 install cookiecutter
```

Second, install docker-compose if you don't already have it:

[docker-compose installation official
docs](https://docs.docker.com/compose/install/).

Then, in the directory you want your project to live:

```bash
cookiecutter gh:ajthr/flask-boilerplate
```

<details><summary>Input Variables</summary>

- project_name [default flask boilerplate]
- project_slug [default flask_boilerplate] - this is your project directory
- mysql_user [default admin] - whether to use any external database like mongodb atlas
- mysql_password [default password]
- mysql_root_password [default root_password]
- mysql_database [default flask_boilerplate]
- secret_key [default super_secret]

</details>

## Develop

Change into your project directory and run:

```bash
docker-compose up -d --build
```

This will build and run the docker containers.

It may take a while to build the first time it's run since it needs to fetch all
the docker images.

Once you've built the images once, you can simply use regular `docker-compose`
commands to manage your development environment, for example to start your
containers:

```bash
docker-compose up -d
```

Once this finishes you can navigate to the localhost port, you should see the slightly modified create-react-app page.

## Testing

To run test for the template, run:

```bash
chmod +x ./test.sh
sudo ./test.sh
```

To run test for api, run
```bash
docker-compose run --rm api sh -c "flask test"
```

[MIT License](LICENSE)
