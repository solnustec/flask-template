FROM python:3.10-alpine

RUN python --version

# Install make
RUN apk add --no-cache make bash

COPY . /src/
WORKDIR /src

# Install Python dependencies
RUN pip install -U pip
RUN pip install -r requirements-dev.txt

EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
