from flask import request
from flask_restful import Resource, reqparse
from model import db, Category, CategorySchema


parser = reqparse.RequestParser()
categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        # print(categories)
        categories = categories_schema.dump(categories)
        # print(help(categories_schema.dump))

        return {'data': categories}


    def post(self):
        json_data = request.get_json(force=True)
        category = Category(
            name=json_data['name']
            )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category)

        return {'data': result }

class SingleCategoryResource(Resource):

    def put(self,id):
        print('id =======', id)
        json_data = request.json
        print('json-data======', json_data)
        category = Category.query.filter_by(id=id).first()
        category.name = json_data.get('name', None)
        db.session.commit()

        result = category_schema.dump(category)

        return { "status": 'success', 'data': result }


    def delete(self,id):
    	json_data = request.json
    	category = Category.query.filter_by(id=id).delete()
    	# category.name = json_data.get('name',None)
    	db.session.commit()
    	result = category_schema.dump(category)
    	return {"data": result}

      




