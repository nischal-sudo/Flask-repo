import sqlite3
from db import db
class UserModel(db.Model):#locked by authenticate and identity
    __tablename__ = "users"


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):#classmethod because of "self.username=username"
        return cls.query.filter_by(username=username).first()#SELECT * FROM users WHERE username=?(table_name=attribute)

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id)
