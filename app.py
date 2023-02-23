from flask import Flask,request,jsonify #paso 6
from flask_sqlalchemy import SQLAlchemy
from models import db, User,MapData
from flask_cors import CORS
from flask_migrate import Migrate
###JWT paso 1
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__) #paso 6
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tapi1740@localhost:5432/testMap'
# Setup the Flask-JWT-Extended extension paso 1
app.config["JWT_SECRET_KEY"] = "kjsfk933321 jjh23214"  #se recomienda poner en el env.py
###########################################
db.init_app(app) ## paso 7
CORS(app)
Migrate(app,db)
jwt = JWTManager(app)

#paso 8 config a app 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Paso 7
@app.route('/create_user',methods = ["POST"])
def create_user():
  user = User()
  user.email = request.json.get("email")
  user.password = request.json.get("password")

  db.session.add(user)
  db.session.commit()

  return jsonify('user created'), 200

# Crea token
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by( email = email,password=password ).first()
    if user is None:
        # the user was not found on the database
      return jsonify({"msg": "Bad email or password"}), 400

    access_token = create_access_token(identity=user.id)
    return jsonify({"token":access_token,"user":user.email,"id":user.id})

# Crear un punto en el mapa, PENDIENTE MODIFICAR QUE SEA BAJO AUORIZACION CON TOKEN
@app.route("/create_mark", methods=["POST"])
@jwt_required()#Lo del token
def create_mark():
  mapdata = MapData()
  current_user_id=get_jwt_identity()
  mapdata.title= request.json.get('title') #
  mapdata.lat = request.json.get('lat') #
  mapdata.long = request.json.get('long') #
  mapdata.date = request.json.get('date') #
  mapdata.id_user_fk = current_user_id #
  mapdata.descrip = request.json.get('descrip') #
  mapdata.amount = request.json.get('amount') #
  mapdata.address = request.json.get('address') #

  db.session.add(mapdata)
  db.session.commit()

  return jsonify(mapdata.serialize()), 200

if __name__ == "__main__": #paso 6
  app.run(host="localhost", port=8080)