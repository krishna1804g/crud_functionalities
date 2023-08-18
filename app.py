from flask import Flask, jsonify
from flask_migrate import Migrate
from db.database import db
from config import ApplicationConfig
from flask_session import Session
from flask_cors import CORS
from main.userRoute import user
from main.cityData import cityData
import csv

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(ApplicationConfig)
app.register_blueprint(user)
app.register_blueprint(cityData)
server_session = Session(app)
db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)