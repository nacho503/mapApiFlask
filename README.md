# Pasos Flask SqlAlchemy

1. app.py : Archivo con la aplicacion principal.
2. models.py : Archivo con los modelos de datos.

- 3. Ejecutar 📢pipenv shell en gitbash.
  - 3.1 📢Para python usar gitbash como terminal.
  - 3.2 📢pipenv shell se va a usar siempre para hacer andar la API.
  - 3.3 ⚠️terminal: pipenv shell Para crear el ambiente virtual, para mantener "encapsulado" el proyecto.

4. Importar e instanciar SQL Alchemy en models.py .

- 5 Crear tablas (User por ejemplo) y cada una lleva 2 funciones:

  - 5.1 funcion 👉repr que nos ayuda a mostrar el objeto cuando queramos debuguearlo.
  - 5.2 funcion 👉serialize que sirve para reresentar los datos o columnas de la tabla.

    ![tabla usuarios](/imagsReadme/tabla_users.JPG)

- 6 Hacer CRUD parte 1:

  - 6.1 En app.py importar fask.
  - 6.2 Instanciar Flask y configurar el puerto.
  - 6.3 Con esto ya podemos levantar el servidor ejecutando en el ⚠️terminal: python app.py (siempre que se haya ejecutado 📢pipenv shell).

    ![app py 1](/imagsReadme/app_py_1.JPG)

- 7 CRUD parte 2:

  - 7.1 Crear rutas en app.py (GET, POST, PUT, DELETE).
  - En app.py importar SQLAlchemy de flask_sqlalchemy y de models, importar db y el modelo (Users).
  - Importar de flask_cors, CORS y de flask_migrate importar Migrate.

    ![importaciones en app.py](/imagsReadme/importaciones1.JPG)

## Instalaciones y dependencias en la terminal:

- En la terminal anteponer ⚠️pipenv install⚠️ para cada uno de los sgtes:
  1. flask-sqlalchemy.
  2. flask flask-migrate.
  3. flask-cors.
