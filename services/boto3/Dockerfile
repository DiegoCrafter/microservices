# se basa en una imagen
FROM python:3.7.0-alpine

# establecemos el directorio de trabajo
WORKDIR /usr/src/app

# copiamos e instalamos las dependencias
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copiamos app
COPY . /usr/src/app

# run server
CMD python manage.py run -h 0.0.0.0