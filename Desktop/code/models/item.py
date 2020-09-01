from db import db

class ItemModel(db.Model):#creates an object which is having name and price properties "db.Model=query"
    __tablename__ = "items"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))#'sqlalchemy.sql.column()'         "#connection"
    price = db.Column(db.Float(precision = 2))

    store_id = db.Column(db.Integer,db.ForeignKey("stores.id"))#tablename.id
    store = db.relationship("StoreModel")#classname in store.py

    def __init__(self,name,price,store_id):#name=row[0],price=row[1]
        self.name=name                                                  #"connection"
        self.price=price
        self.store_id=store_id

    def json(self):
        return {"name":self.name,"price":self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()#that db name=this name what we have given
#"query" is not something we defibne ,that comes from "db.Model"

    #classmethodbecause self.insert(item) is used above
    def save_to_db(self):
        db.session.add(self)#INSERT INTO items VALUES
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
