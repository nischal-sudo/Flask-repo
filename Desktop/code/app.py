import os
from flask import Flask,request
from flask_restful import Api#An(API) is a set of routines, protocols, and tools for building software applications.
# Basically, an API specifies how software components should interact
from flask_jwt import JWT #security purpose 1

from resources.item import Item,ItemList
from security import authenticate,identity #inheriting
from resources.user import UserRegister
from resources.store import Store,StoreList

app=Flask(__name__)#"creating" a flask app
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL","sqlite:///data.db")#2#where to find "data.db" file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False#SQLAlchemy has its own track modification
app.secret_key = "jose"#security purpose 2
api = Api(app)#a set of functions and procedures "allowing" the creation of applications,creating Api app

jwt = JWT(app,authenticate,identity)#/auth

api.add_resource(Store,"/store/<string:name>")
api.add_resource(Item,"/item/<string:name>")
api.add_resource(StoreList,"/stores")
api.add_resource(ItemList,"/items")
api.add_resource(UserRegister,"/register")

if __name__ == "__main__": #only the file we run is the main
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
