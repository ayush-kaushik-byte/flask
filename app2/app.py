from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.secret_key = 'Ayush'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
	"""docstring for Student"""

	parser = reqparse.RequestParser() # for specifying fields in request.
	parser.add_argument('price',
		type=float,
		required=True,
		help='This field cannot be left blank.'
		)

	@jwt_required()
	def get(self, name):
		# for item in items:
		# 	if item['name'] == name:
		# 		return item
		item = next(filter(lambda x: x['name'] == name, items), None)

		return {'item': item}, 200 if item is not None else 404

	@jwt_required()
	def post(self, name):

		if next(filter(lambda x: x['name'] == name, items), None) is not None:
			return {'message': 'item already present'}, 404
		else:
			data = Item.parser.parse_args()
			item = {'name': name, 'price': data['price']}
			items.append(item)
			return item, 201

	@jwt_required()
	def delete(self, name):
		for item in items:
			if item['name'] == name:
				items.remove(item)
				return {'message': f'{name} removed!!!'}, 200

		return {'message': f'Item {name} not found!!'}, 404

	@jwt_required()
	def put(self, name):

		data = Item.parser.parse_args()

		item = next(filter(lambda x: x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else:
			item.update(data)
		return item, 200

class ItemList(Resource):

	@jwt_required()
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)		