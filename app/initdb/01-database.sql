# create databases
CREATE DATABASE IF NOT EXISTS `app`;

# grant all privilages to admin
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
