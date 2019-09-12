from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import *
from resources.Book import *



category_app = Blueprint('category', __name__)
api = Api(category_app)



api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Categories')
api.add_resource(SingleCategoryResource, '/Category/<id>')
api.add_resource(BookResource, '/Books')
api.add_resource(SingleBookResource, '/Books/<id>')