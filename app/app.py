from config import app, db

# register blueprints here

# example route
@app.get("/")
def home():
    return "Flask Boilerplate v0.1.0", 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()
