from flask import Flask,request,jsonify #paso 6
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__) #paso 6
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tapi1740@localhost:5432/testMap'
db.init_app(app) ## paso 7
CORS(app)
Migrate(app,db)

#paso 8 config a app 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Paso 7
@app.route('/', methods=["GET"]) #GET, POST, PUT, DELETE
def home():
  return 'Hello Flask API'

@app.route('/create_user',methods = ["POST"])
def create_user():
  user = User()
  user.email = request.json.get("email")
  user.password = request.json.get("password")

  db.session.add(user)
  db.session.commit()

  return jsonify('user created'), 200

if __name__ == "__main__": #paso 6
  app.run(host="localhost", port=8080)