
### Docker

Run the following to quick build everything necessary to run the application in dev:
```
docker-compose -f docker/docker-compose.yml build geolocation-service
```

and the for starting the API:
```
docker-compose -f docker/docker-compose.yml up
```

### Local

Run the following command to run the migrations:
```
poetry run alembic -c app/alembic.ini revision --autogenerate
```
and then run this to apply the new schema to the database:
```
poetry run alembic -c app/alembic.ini upgrade head
```

To run the .csv loader application:
```
poetry run python -m app.data_library.data_loader
```

To run isort on the code:
```
poetry run isort --settings-path ./pyproject.toml --recursive 
```

To run black:
```
poetry run black --config pyproject.toml .
```

To run tests:
```
poetry run pytest ./tests
```