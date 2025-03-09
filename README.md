# @solnustec/flask-template

First, you need to change the project name in the following files:

- `sonar-project.properties`
- `app/config/settings.py`
- `local.yml`
- `README.md`

## Requirements

You need to install the following dependencies.

1. [Python](https://www.python.org/): the min version required is `3.10`

2. [Docker](https://docker.com): recommended in the latest version

3. [Git](https://git-scm.com/): recommended in the latest version

## Set-up

- Run `docker compose -f local.yml build` in the root directory. This going to install all
  the required packages.
- Run `docker compose -f local.yml up` to start the server on port `8080`
- Enjoy! 😊

To configure the project, you must create an .env file by copying the provided `back.env` template:

```sh
cp back.env .env
```
Then, update the .env file with the following environment variables:


## Running Tests & Code Formatting

Common commands for development tasks are available in the `Makefile`. To run them, use:

```sh
make <command>
```

### **Testing & Linting**
Commands for running tests and ensuring code quality.

- `make lint` → Format code using `black` and `isort`.
- `make lint-check` → Check code formatting without modifying files. Also runs `flake8` for linting.

### **Pre-Push Checks**
Ensure code quality and fix issues before pushing changes.

- `make pre-push-fix` → Auto-fix backend issues using predefined scripts.
- `make pre-push` → Run validation checks before pushing to GitHub.

