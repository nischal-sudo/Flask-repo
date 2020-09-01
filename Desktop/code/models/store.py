from db import db

class StoreModel(db.Model):#creates an object which is having name and price properties #"query"
    __tablename__ = "stores"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))#'sqlalchemy.sql.column()'

    items = db.relationship("ItemModel",lazy="dynamic")

    def __init__(self,name):#name=row[0],price=row[1]
        self.name=name

    def json(self):
        return {"name":self.name,"items":[item.json() for item in self.items]}

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
