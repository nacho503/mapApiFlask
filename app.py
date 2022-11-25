from flask import Flask #paso 6
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__) #paso 6

#Paso 7
@app.route('/', methods=["GET"]) #GET, POST, PUT, DELETE
def home():
  return 'Hello Flask API'

if __name__ == "__main__": #paso 6
  app.run(host="localhost", port=8080)