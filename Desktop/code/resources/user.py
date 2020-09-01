import sqlite3
from flask_restful import Resource,reqparse#Parser is a compiler that is used to break the data into smaller elements
from models.user import UserModel

class UserRegister(Resource):#new register(Sign upp)
    parser = reqparse.RequestParser()
    parser.add_argument("username",
    type = str,
    required = True,
    help = "This could not be empty")
    #request object in Flask.
    parser.add_argument("password",
    type = str,
    required = True,
    help = "This could not be empty")

    def post(self):
        data = UserRegister.parser.parse_args()#classname.paser.parse_args()
        if UserModel.find_by_username(data["username"]):#above connection
            return {"messege":"A user with that username already exists."},400

        user = UserModel(data["username"],data["password"])#or (**data)
        user.save_to_db()
        return {"message":"User created successfully"},201
