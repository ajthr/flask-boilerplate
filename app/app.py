from config import app, db

# register blueprints here

@app.route("/", methods=["GET"])
def home():
    return "Flask Boilerplate v0.1.0", 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()
