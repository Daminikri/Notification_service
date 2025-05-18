# from app import app, db

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
    
from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # run inside app context
    app.run(debug=True)
