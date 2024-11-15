from app import create_app, db
from app.database import populate_database

app = create_app()

@app.before_first_request
def setup_database():
    db.create_all()
    populate_database()
if __name__ == "__main__":
    app.run()
