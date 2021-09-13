# This script will be executed when a new database container is started.
# creates multiple databases in the same container.

# create databases
CREATE DATABASE IF NOT EXISTS `{{ cookiecutter.project_slug }}`;
CREATE DATABASE IF NOT EXISTS `tests`;

# grant all privilages to user
GRANT ALL PRIVILEGES ON *.* TO '{{ cookiecutter.mysql_user }}'@'%';
