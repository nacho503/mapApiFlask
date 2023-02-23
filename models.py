from flask_sqlalchemy import SQLAlchemy #paso 4
db = SQLAlchemy() # paso 4

class User(db.Model): # paso 5
  id = db.Column(db.Integer, primary_key=True)
  email= db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(10), nullable=False)

  mapdata = db.relationship('MapData',backref='user',lazy=True)

  def __repr__(self):
    return "<User %r>" %self.email
  
  def serialize(self):
    return{
      "id":self.id,
      "email":self.email,
      "password":self.password
    }
  
class MapData(db.Model): #id, titulo, lat, long, fecha, id_user_fk, descrip, monto, direccion
  id = db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(30),nullable=False)
  lat = db.Column(db.Float,nullable=False) #db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None)
  long = db.Column(db.Float,nullable=False) 
  date= db.Column(db.String(11),nullable=False) #worked previously with 
  id_user_fk=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  descrip=db.Column(db.String(999),nullable=False)
  amount = db.Column(db.Integer,nullable=True)#Puede ser nulo para dar opcion de precio a convenir
  address = db.Column(db.String(100),nullable=False)

  def __repr__(self):
    return "<Tittle %r>" %self.tittle

  def serialize(self):
    return{
      "id":self.id,
      "title":self.title,
      "lat":self.lat,
      "long":self.long,
      "date":self.date,
      "id_user_fk":self.id_user_fk,
      "descrip":self.descrip,
      "amount":self.amount,
      "address":self.address,
      "user_email" :self.user.email
    }
