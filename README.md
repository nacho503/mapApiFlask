# Pasos Flask SqlAlchemy

1. app.py : Archivo con la aplicacion principal.
2. models.py : Archivo con los modelos de datos.

- 3 Ejecutar 📢pipenv shell en gitbash.
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
  - 7.2 En app.py importar SQLAlchemy de flask_sqlalchemy y de models, importar db y el modelo (Users).
  - 7.3 Importar de flask_cors, CORS y de flask_migrate importar Migrate.
  - 7.4 Configuraciones extras db.init(app), CORS(app), Migrate(app,db).

    - 7.4.1 CORS es para los permisos CORS, Migrate guarda la estructura de la 💻bbdd.

    ![importaciones en app.py](/imagsReadme/importaciones1.JPG)

- 8 CRUD parte 3, app config:

  - 8.1 Track modifications a false para que no muestre los cambios en el log.
  - 8.2 URI de postgre : dialect://username:password@host:port/database
  - Se importa request y jsonify para mostrar al usuario las consultas.

- 9 Pasos para que se cree, reconozca la bbdd:
  - Nota 🚨error "RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set."
  - 🧑‍🔧Se arreglo moviendo el app.config despues del app=FLASK(**name**)
  - Se importo psycopg2-binary
  - 9.1 En la ⚠️terminal:
    - 9.1.1 flask db init (dio error de la nota)
    - 9.1.2 flask db migrate
    - 9.1.3 flask db upgrade

## Instalaciones y dependencias en la terminal:

- En la terminal anteponer ⚠️pipenv install⚠️ para cada uno de los sgtes:
  1. flask-sqlalchemy.
  2. flask flask-migrate.
  3. flask-cors.
  4. psycopg2-binary

## Para arrancar la BBDD:

- Asegurarse que se hizo en la ⚠️terminal de git bash⚠️ pipenv shell, aplicar pasos del 9.1
