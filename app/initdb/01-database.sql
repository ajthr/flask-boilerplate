# This script will be executed when a new database container is started.
# creates multiple databases in the same container.

# create databases
CREATE DATABASE IF NOT EXISTS `app`;
CREATE DATABASE IF NOT EXISTS `tests`;

# grant all privilages to admin
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
