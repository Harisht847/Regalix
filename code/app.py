from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.Item import Book, ItemList
from db import db
app = Flask(__name__)
db.init_app(app)
POSTGRES = {
        'db': 'library',
        'user': 'postgres',
        'pw':'Winter05',
        'host':'localhost',
        'port': '5432',
    }



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = 'Harish'

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # ===>> it will create new endpopint /auth for validation


'''
class Student(Resource):
    def get(self, name):
        return {'student':name}

'''

#api.add_resource(Student, "/student/<string:name>")
api.add_resource(Book, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/userregister")


if __name__ == '__main__':

    app.run(port=5000)
