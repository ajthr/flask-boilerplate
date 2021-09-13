#!/bin/bash

# Exit in case of error
set -e

# Run this from the root of the project
cookiecutter --no-input -f ./ project_name="test"

cd test

docker-compose build
docker-compose down -v --remove-orphans
docker-compose up -d

# Run tests
docker-compose run --rm app sh -c "flask test"

# Cleanup
docker-compose down -v --remove-orphans
cd ..
rm -rf test

# Print result
echo -e "\033[0;32m Test Passed."
