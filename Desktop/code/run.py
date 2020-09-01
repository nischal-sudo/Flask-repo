from app import app
from db import db

db.init_app(app)

@app.before_first_request#1 it runs before the first request whtaever it may be
def create_tables():
    db.create_all()
