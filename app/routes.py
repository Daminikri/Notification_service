from flask import request, jsonify
from app import app, db
from app.models import Notification
import json, pika

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    notif = Notification(user_id=data['userId'], type=data['type'], message=data['message'])
    db.session.add(notif)
    db.session.commit()

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps({"id": notif.id}))
    connection.close()

    return jsonify({"status": "queued", "notificationId": notif.id})

@app.route('/users/<string:user_id>/notifications', methods=['GET'])
def get_user_notifications(user_id):
    notifs = Notification.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'notificationId': n.id,
        'type': n.type,
        'message': n.message,
        'status': n.status,
        'timestamp': n.timestamp.isoformat()
    } for n in notifs])