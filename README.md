# Notification Service

## Objective
Build a system to send Email, SMS, and In-App notifications.

## Features
- REST APIs for sending and fetching notifications
- Types: Email, SMS, In-App
- Queued processing with RabbitMQ
- Retry logic for failed notifications

## Technologies Used
- Flask (Python web framework)
- SQLite (lightweight DB, can be swapped)
- RabbitMQ (asynchronous message queue)
- Pika (RabbitMQ client for Python)

## Folder Structure
```
notification_service/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── worker.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd notification_service
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run RabbitMQ (using Docker)
```bash
docker run -d --hostname rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
``` 

### 4. Run Flask API server
```bash
python main.py
```

### 5. Run the worker in a separate terminal
```bash
python app/worker.py
```

## API Usage

### POST `/notifications`
Send a notification to a user.
```json
{
  "userId": "123",
  "type": "email",
  "message": "Welcome to the app!"
}
```

### GET `/users/{id}/notifications`
Fetch all notifications for a specific user.

### Assumptions
Email, SMS, and In-App notifications are simulated via print statements.
SQLite is used for simplicity; it can be replaced with PostgreSQL/MySQL.
RabbitMQ must be running locally via Docker or system install.

###  Postman API Collection

Use this link to test the API using Postman:

🔗 [Notification Service Postman Collection](<https://www.postman.com/spaceflight-architect-61823832/notification-service/collection/qxeqlyy/new-collection?action=share&creator=43293695>)
