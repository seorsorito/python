
from flask_login import UserMixin,LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

login_manager=LoginManager()
db=SQLAlchemy()

class User(UserMixin,db.Model):

    __tablename__="Mis_usuarios"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    email=db.Column(db.String(100),unique=True,nullable=False) #con unique nos aseguramos que no se repitan emails,nullable que no se puede dejar el campo vacio
    password=db.Column(db.String(500),nullable=False)
    is_admin=db.Column(db.Boolean, default=False)
    
    
    def set_password(self,password):

        self.password=generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)
        #return self.password #remedio temporal

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

    
"""users=[] #remedio mientras no uso BBDD

def get_user(email):
    for user in users:
        if user.email==email:
            return user 
    
    return None"""