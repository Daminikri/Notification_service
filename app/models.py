from app import db
from datetime import datetime

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # email, sms, in-app
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='queued')
    retries = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)