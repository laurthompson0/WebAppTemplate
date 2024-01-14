# Full Stack Web App Template

## To Run

```bash
# create db volume directories
mkdir db/pg/data
mkdir db/pg/data/dev
mkdir db/pg/data/prod

# create env file
cp _env_templates/dev.env .env

# run
docker compose up
```

Browse to `http://localhost:81`

## About

### Stack

This repository contains all the necessary components to run a `dockerized` full stack web application in a development environment.

- Gatway/Routing: `NGINX`
- User Interface: `React-ts` with `VITE` for environment management
- Backend: `Python` with `FastAPI`
- Database: `Postgres`

Possible (Not Included) Extensions

- Queueing
- NoSQL DBs
- HTTPS

### Assumptions

- `Docker-compose` is already installed on the host machine

### Notes and Recommendations

- The `docker-compose.override.yml` exists for development purposed only. It defines volumes for `app` and `ui` that point directly to the source files, and specifies watching/reloading of the source, allowing you to develop while the containers are running and have those changes reflected directly in the app.
- The full stack is currently deployed with a single `repo`, a single `docker-compose.yml`, a single `.env` file. However, it is recommended that you break each component up into its own microservice. To assist with this process, each subdirectory already contains `.env` templates for that service. The `docker-compose.yml` can be broken up by moving each service into its own file compose file. When doing so, I recommend defining the network with the `gw` (gateway/NGINX) service, and having all other services attach to that as an external network.
- You do not need to locally install the yarn/pip dependencies/environment because everyting is run in containers. However, depending on your editor, the editor likely will not be able to see the dependencies so imports and syntax highlighting will look very angry unless you install the environment outside of docker as well.
- The `prod` environment assumes two things.

  1. The `docker-compose.override.yml` is not present (can be renamed as `docker-compose.dev.yml`)
  2. There is some docker repository from which the production images can be pulled.

  For this template, I do not go into the details of creating/pushing/pulling production docker images. This will likely be an environment-specific process.

- HTTPS is not currently supported by this template, but all components of this template support HTTPS, so it is possible to add.
