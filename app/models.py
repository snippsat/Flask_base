from .extensions import db
from datetime import datetime

class Message(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    input_field = db.Column(db.String(240), nullable=False)
    email = db.Column(db.String(240), nullable=False)
    message = db.Column(db.String(2048), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)