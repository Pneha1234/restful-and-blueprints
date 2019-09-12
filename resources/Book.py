from flask import jsonify, request
from flask_restful import Resource,reqparse
from model import *

books_schema = BookSchema(many=True)
book_schema = BookSchema()

parser = reqparse.RequestParser()

class BookResource(Resource):
    def get(self):
        books = Book.query.all()
        books = books_schema.dump(books).data
        return {"data":books}

    def post(self):

        json_data = request.get_json(force=True)
        print('json-data======', json_data)
        book = Book(
            category_id=json_data['category_id'], 
            book=json_data['book']

            )

        db.session.add(book)
        db.session.commit()

        result = book_schema.dump(book)

        return {'data': result}

class SingleBookResource(Resource):

    def put(self,id):
        print('id =======', id)
        json_data = request.json
        print('json-data======', json_data)
        book = Book.query.filter_by(id=id).first()
        book.book = json_data.get('book', None)
        db.session.commit()

        result = book_schema.dump(books)

        return { "status": 'success', 'data': result }


    def delete(self,id):
        json_data = request.json
        book= Book.query.filter_by(id=id).delete()
        # category.name = json_data.get('name',None)
        db.session.commit()
        result = book_schema.dump(book)
        return {"data": result}
