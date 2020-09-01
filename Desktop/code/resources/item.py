from flask_restful import Resource ,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):#retrive item from database
    parser = reqparse.RequestParser()
    parser.add_argument("price",
    type = float,
    required=True,
    help = "This field cannot be blank")

    parser.add_argument("store_id",
    type = float,
    required=True,
    help = "Every item needs a store ID.")

    @jwt_required() #must
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"Item not found"},404

    def post(self,name):
        if ItemModel.find_by_name(name):#check items not in database
            return {"message":"An item of {} already exists.".format(name)},400
        data = Item.parser.parse_args()#parse data using parser
        item = ItemModel(name,data["price"],data["store_id"]) #make one item or "**data"
        try:
            item.save_to_db()
        except:
            {"message":"Internal server error"},500

        return item.json(),201

    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item :
            item.delete_from_db()
        else:
            return {"messege":"Item not found of that name"}

        return {"message":"Item deleted"}

    def put(self,name):
        data = Item.parser.parse_args()
        item=ItemModel.find_by_name(name)#the old
        if item is None:#if no item in items "create"
            item = ItemModel(name,data["price"],data["store_id"])
        else:
            item.price = data["price"]#that name of price modification

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items":[items.json() for items in ItemModel.query.all()]}
