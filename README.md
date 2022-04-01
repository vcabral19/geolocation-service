# Gelocation over IP Service

### This repo is relative to an API that returns Geolocations over a valid IP address

Poetry managed Python FastAPI application with Docker multi-stage builds.

This application uses docker-compose for development and Postgresql as a database.

There is a very simple CI/CD pipeline for github actions under ".git" folder.

Although you can start playing with the API immediately with the docker-compose command you should first import the data in a separate step described bellow.

### Requirements

- [Docker >= 17.05](https://docs.docker.com/get-docker/)
- [Docker Compose>= 1.29.2](https://docs.docker.com/compose/install/)
- [Python >= 3.8](https://www.python.org/downloads/release/python-381/)
- [Poetry](https://github.com/python-poetry/poetry)


---
**NOTE** - Run all commands from the project root

##tl;dr

### Start Application
Run the following to quick build everything necessary to run the application in dev:
```
docker-compose -f docker/docker-compose.yml build geolocation-service
```

and the for starting the API:
```
docker-compose -f docker/docker-compose.yml up
```

### Import Data
To populate the database:

1. Write your .csv dataset in the data/ folder in the root of the project
2. Update (if necessary) app/config/config_dev.ini CSV_PATH variable
3. Rebuild your image and then run:
```
docker exec geolocation-service python -m app.data_library.data_loader
```


## Local development

---
## Poetry


Create the virtual environment and install dependencies with:

        poetry install

See the [poetry docs](https://python-poetry.org/docs/) for information on how to add/update dependencies.

Run commands inside the virtual environment with:

        poetry run <your_command>

Spawn a shell inside the virtual environment with

        poetry shell

Start a development server locally

        poetry run uvicorn app.main:app --reload --host localhost --port 8000

API will be available at [localhost:8000/](http://localhost:8000/)

Swagger docs at [localhost:8000/docs](http://localhost:8000/docs)

But you will need a PostgreSQL instance up and running before doing that:

```
docker run --name postgresql-container -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```

---

## Docker


Build images with:
        
        docker build --tag geolocation-service --file docker/Dockerfile . 

The Dockerfile uses multi-stage builds to run lint and test stages before building the production stage.  If linting or testing fails the build will fail.

You can stop the build at specific stages with the `--target` option:

        docker build --name geolocation-service --file docker/Dockerfile . --target <stage>


For example, we wanted to stop at the **test** stage:

        docker build --tag geolocation-service --file docker/Dockerfile --target test .

We could then get a shell inside the container with:

        docker run -it geolocation-service:latest bash

If you do not specify a target the resulting image will be the last image defined which in our case is the 'production' image.

For a database you can use the same docker container described in the end of the poetry instructions section for development.

And you can always stick to the docker-compose option described in the TL;DR session for a faster flow.


## Other Instructions

Check the other doc (util_commands.md) for other useful commands when operating the application

## Next Steps and Limitations

In respect of time there is a lot that I have compromised when writing the application.
Nevertheless, I consider this version viable as a first product given my constraints.

Some limitations I'm already aware of that I would work next if I could:

---
* Write async version of the get "/geolocation/{ip_address}" ;
* For doing this we should also change the way the DB client is managed today, to allow the queries to Postgresql executed by SQLAlachemy to be async.
---
* There is no configs file for prod and staging for obvious reasons.
---
* The "data_library" is not really a lib that could be packaged and deployed separately right now as it has some dependencies on other namespaces of the project ;
* This especially because of the "data_loader" application which I would probably refactor to another place to be a consumer of the "data_library";
* Also, the pydantic model "schema_geolocation" might be moved to away of the lib to be closer to the API itself.
---
* Finally, regarding performance of the exporter, it loads the whole dataset extracted from the .csv into memory;
* This is of course does not scale well for too big datasets (.csv files potentially bigger than commodity hardware memory, lets say 8gigs) ;
* So I would introduce a configurable threshold on the buffer to bulk dump records as soon as this limit is achieved;
* Another issue with this is that we would need to change the data model to allow de-duplication of the records in some other form as it's really hard to de-duplicate records without having access to all of them in memory.
---
Finally, I would love to re-write this app in a language with better computational performance. Let's say for example, Go :)

