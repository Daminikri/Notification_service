import pika, json, time
from app import app, db
from app.models import Notification

RETRY_LIMIT = 3

with app.app_context():
    def callback(ch, method, properties, body):
        data = json.loads(body)
        notif = db.session.get(Notification, data['id'])  # updated for SQLAlchemy 2.0+

        if not notif:
            print(f"[!] Notification with ID {data['id']} not found.")
            return

        try:
            # Simulate type-specific processing
            if notif.type == 'email':
                print(f"[📧] Sending EMAIL to user {notif.user_id}: {notif.message}")
            elif notif.type == 'sms':
                print(f"[📱] Sending SMS to user {notif.user_id}: {notif.message}")
            elif notif.type == 'in-app':
                print(f"[💬] In-App Notification for user {notif.user_id}: {notif.message}")
            else:
                print(f"[❌] Unknown notification type: {notif.type}")
                notif.status = 'failed'
                db.session.commit()
                return

            time.sleep(1)  # simulate sending delay
            notif.status = 'delivered'

        except Exception as e:
            print(f"[!] Error while sending notification: {e}")
            notif.retries += 1
            if notif.retries >= RETRY_LIMIT:
                notif.status = 'failed'

        db.session.commit()

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)

    print("Worker started. Waiting for messages...")
    channel.start_consuming()
