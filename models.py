from flask_sqlalchemy import SQLAlchemy #paso 4
db = SQLAlchemy() # paso 4

class User(db.Model): # paso 5
  id = db.Column(db.Integer, primary_key=True)
  email= db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(10), nullable=False)

  def __repr__(self):
    return "<User %r>" %self.email
  
  def serialize(self):
    return{
      "id":self.id,
      "email":self.email,
      "password":self.password
    }