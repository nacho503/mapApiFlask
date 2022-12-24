from flask_sqlalchemy import SQLAlchemy #paso 4
db = SQLAlchemy() # paso 4

class User(db.Model): # paso 5
  id = db.Column(db.Integer, primary_key=True)
  email= db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(10), nullable=False)

  mapa = db.relationship('Mapa',backref='user',lazy=True)

  def __repr__(self):
    return "<User %r>" %self.email
  
  def serialize(self):
    return{
      "id":self.id,
      "email":self.email,
      "password":self.password
    }
  
class Mapa(db.Model): #id, titulo, lat, long, fecha, id_user_fk, descrip, monto, direccion
  id = db.Column(db.Integer, primary_key=True)
  titulo=db.Column(db.String(30),nullable=False)
  lat = db.Column(db.Float,nullable=False) #db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None)
  long = db.Column(db.Float,nullable=False) 
  fecha= db.Column(db.DateTime(250),nullable=True)
  id_user_fk=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  descrip=db.Column(db.String(999),nullable=False)
  monto = db.Column(db.Integer,nullable=True)#Puede ser nulo para dar opcion de precio a convenir
  direccion = db.Column(db.String(100),nullable=False)

  def __repr__(self):
    return "<Titulo %r>" %self.titulo

  def serialize(self):
    return{
      "id":self.id,
      "titulo":self.titulo,
      "lat":self.lat,
      "long":self.long,
      "fecha":self.fecha,
      "id_user_fk":self.id_user_fk,
      "descrip":self.descrip,
      "monto":self.monto,
      "direccion":self.direccion,
      "user_email" :self.user.email
    }
