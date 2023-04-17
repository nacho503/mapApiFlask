### PASAR TODO A INGLES

# Data Model:

- Add img when difinitive model is ready.

# Routes:

1. create_user : POST for user.
2. login: POST for login and gives user data + JWT token.
3. create_mark: POST for putting a dot with data in the Map.

# Steps for FLASk SQLALCHEMY

1. app.py : Main app file.
2. models.py : Data model.

- 3 Execute 📢pipenv shell in gitbash.
  - 3.1 📢for python use gitbash in the terminal.
  - 3.2 📢pipenv shell always for running the API.
  - 3.3 ⚠️terminal: pipenv shell for creating the virtual ambient, it "encapsulates" the project.

4. Import & instantiate SQLAlchemy in models.py.

- 5 Create tables (User, MapData) and each with two functions:

  - 5.1 👉repr: It shows the object so it is easier to debug it.
  - 5.2 👉serialize: Which shows the created object.

    ![tabla usuarios](/imagsReadme/tabla_users.JPG)

- 6 Steps for building CRUD part 1:

  - 6.1 On app.py import flask.
  - 6.2 Instance Flask and configure port.
  - 6.3 Execute: ⚠️terminal: python app.py and it is ready for use (after 📢pipenv shell), follow next steps...

    ![app py 1](/imagsReadme/app_py_1.JPG)

- 7 CRUD part 2:

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
  - Se instalo psycopg2-binary
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

## To run DB:

- Make sure that on ⚠️terminal git bash⚠️ pipenv shell was done, aplicar pasos del 9.1.
- ⚠️⚠️⚠️Cada vez que se modifique el modelo, eliminar y crear denuevo en el PGadmin y aplicar los comandos del 9.1 (estando con pipenv shell)

# JWT

1. ⚠️pipenv install, importaciones y el setup 🔗(https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/):

- Nota: Se recomienda poner la variable del app.config["JWT_SECRET_KEY"]=VARIABLE en el archivo de env.py.
- Nota: Se volvieron a instalar las dependencias anteriores pero ahora con el pip install...
- 1.1 pip install Flask-JWT
- 1.2 pip install Flask-JWT-Extended

2. Ruta LOGIN con POST para crear token
