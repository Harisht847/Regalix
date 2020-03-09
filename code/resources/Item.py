from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.item import LibraryModel

class Book(Resource):
    TABLE_NAME = 'library'
    parser = reqparse.RequestParser()
    #parser.add_argument('id',type =int, required=True, help = "Every items need a store id")
    #parser.add_argument('name',type =str, required=True, help = "This field cannot be blank!!")
    parser.add_argument('available',type =str, required=True, help = "This field cannot be blank!!")



    @jwt_required()
    def get(self,name):
        item = LibraryModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"Item not found"}, 404

    def post(self,name):
        if LibraryModel.find_by_name(name):
            return {'message':'An item with the name {} is already exsisted'.format(name)}, 400
        data = Book.parser.parse_args()
        item = LibraryModel(name=name, available=data['available'])
        #try:
            #item.insert()
        item.save_to_db()
        #except:
            #return {"message": "An error occurred inserting the item."}, 500
        return item.json()


    def delete(self,name):
        item = LibraryModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message':'Item has been deleted'}
        return {'message':'Item does not existed'}


    def put(self, name):

        data = Book.parser.parse_args()
        item = LibraryModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])
        if item is None:
            item = LibraryModel(name=name, available=data['available'])
        else:
            item.available= data['available']
            item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):


        #return {"result":[item.json() for item in LibraryModel.query.all()]}
        return {"result":list(map(lambda x: x.json(), LibraryModel.query.all()))}
