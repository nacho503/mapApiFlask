# Pasos Flask SqlAlchemy

1. app.py : Archivo con la aplicacion principal.
2. models.py : Archivo con los modelos de datos.

- 3. Ejecutar 📢pipenv shell en gitbash.
  - 3.1 📢Para python usar gitbash como terminal.
  - 3.2 📢pipenv shell se va a usar siempre para hacer andar la API.
  - 3.3 ⚠️terminal: pipenv shell Para crear el ambiente virtual, para mantener "encapsulado" el proyecto.

4. Importar e instanciar SQL Alchemy en models.py .

- 5. Crear tablas (User por ejemplo) y cada una lleva 2 funciones:
  - 5.1 funcion 👉repr que nos ayuda a mostrar el objeto cuando queramos debuguearlo.
  - 5.2 funcion 👉serialize que sirve para reresentar los datos o columnas de la tabla.

## Instalaciones y dependencias en la terminal:

- En la terminal anteponer ⚠️pipenv install⚠️ para cada uno de los sgtes:
  1. flask-sqlalchemy.
  2. flask flask-migrate.
  3. flask-cors.
