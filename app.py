from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
# Exceptions are re-raised rather than being handled by the app’s error handlers. 
# #If not set, this is implicitly true if TESTING or DEBUG is enabled.
app.config['PROPAGATE_EXCEPTIONS'] = True
# A secret key that will be used for securely signing the session cookie and can 
# # be used for any other security related needs by your application
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
