from db.database import db
from flask_marshmallow import Marshmallow
from uuid import uuid4

# unique id generation
def get_uuid():
    return uuid4().hex

ma = Marshmallow()

class User(db.Model):
    
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(32))
    admin_role = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(354), unique=True)
    password = db.Column(db.Text, nullable=False)
    ph_number = db.Column(db.Integer)
    city = db.Column(db.String(32))
    State = db.Column(db.String(32))
    community = db.Column(db.String(32))

    def __init__(self, email, password, ph_number, username, admin_role, city, state, community):
        self.email = email
        self.password = password
        self.ph_number = ph_number
        self.username = username
        self.admin_role = admin_role
        self.city = city
        self.state = state
        self.community = community
        
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'ph_number', 'username', 'admin_role', 'city', 'state', 'community')

user_schema = UserSchema()
users_schema = UserSchema(many=True)