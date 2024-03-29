from flask_sqlalchemy import SQLAlchemy #paso 4
db = SQLAlchemy() # paso 4

class User(db.Model): # paso 5
  id = db.Column(db.Integer, primary_key=True)
  email= db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(10), nullable=False)
  user_name = db.Column(db.String(20), nullable=False)

  mapdata = db.relationship('MapData',backref='user',lazy=True)

  def __repr__(self):
    return "<User %r>" %self.email
  
  def serialize(self):
    return{
      "id":self.id,
      "email":self.email,
      "password":self.password,
      "user_name": self.user_name
    }
  
class MapData(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(30),nullable=False)
  lat = db.Column(db.Float,nullable=False) 
  long = db.Column(db.Float,nullable=False) 
  date= db.Column(db.String(11),nullable=False) 
  id_user_fk=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  descrip=db.Column(db.String(999),nullable=False)
  amount = db.Column(db.Integer,nullable=True)
  address = db.Column(db.String(100),nullable=False)
  cluster_number_ = db.Column(db.Integer, db.ForeignKey('map_cluster.id'), nullable=True) #Refference to the cluster of points

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
      "user_email" :self.user.email,
      "user_name": self.user.user_name,
      "cluster_number":self.cluster_number_
    }

  class MapCluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cluster_number = db.Column(db.Integer, nullable=False)
    cluster_lat = db.Column(db.Float, nullable=False)
    cluster_long = db.Column(db.Float, nullable=False)
    map_data_id = db.Column(db.Integer, db.ForeignKey('map_data.id'), nullable=False)
    # Define a many-to-one relationship with MapData model
    map_data = db.relationship('MapData', backref=db.backref('clusters', lazy=True))

  def __repr__(self):
    return "<Tittle %r>" %self.cluster_number

  def serialize(self):
    return{
      "id":self.id,
      "cluster_number":self.cluster_number,
      "cluster_long":self.cluster_long,
      "cluster_lat":self.cluster_lat,
      "map_data_id":self.map_data_id,
      "map_data_title": self.mapdata.title
    }