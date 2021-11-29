import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from recourses.user import UserRegister
from recourses.item import Item, ItemList
from recourses.store import Store, StoreList

db_uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'george'
api = Api(app)

jwt = JWT(app, authenticate, identify)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':

    app.run(port=5000, debug=True)
