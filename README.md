# flask-boilerplate
Flask Restful API Boilerplate

### what does flask-boilerplate include

- Custom commands for ease of use
    - init        - Adds a migrations folder to the application.
    - migrate     - Generates an initial migration.
    - upgrade     - Applies the migration to the database.
    - runserver   - Start the application server.
    - test        - Run tests for the application.
- Mysql for db
    - Mysql is configured and ready to be used.
- Project structure
    - Related files can be grouped.
    - Components can be isolated. 
- Dockerized

## Running the project

### with docker

- create a .env file in the working directory and add environment variables.
    ```
    DB_ADMIN_USER=user
    DB_ADMIN_PWD=userpwd
    DB_ROOT_PWD=rootpwd
    ```
- Build services:\
    `docker-compose build`
- Run the project:\
    `docker-compose up`

### without docker

- make sure mysql is installed in the system.
- clone repo and go to the project's directory.
- install the dependencies:\
    `pip install -r requirements.txt`
- Run the migrations:\
    `python manage.py init && python manage.py migrate && python manage.py upgrade`
- Run the project:\
    `python manage.py runserver`

## Testing

- Run tests with:\
    `docker exec -it app sh -c "python manage.py test"`

Copyright (c) 2021 Ajith Ramachandran

[MIT License](LICENSE)
