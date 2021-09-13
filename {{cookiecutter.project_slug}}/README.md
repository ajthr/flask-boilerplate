# {{ cookiecutter.project_name }}

## Quick Start

Change into your project directory and run:

```bash
docker-compose up -d --build
```

This will build and run the docker containers.

It may take a while to build the first time it's run since it needs to fetch all
the docker images.

To start containers without building, run:

```bash
docker-compose up -d
```

Once this finishes you can navigate to the localhost port, you should see the slightly modified create-react-app page.

## Testing

To run tests
```bash
docker-compose run --rm api sh -c "flask test"
```
