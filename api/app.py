# api/app.py

from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from random import randint

es = Elasticsearch(['http://elasticsearch:9200'])
app = Flask(__name__)

# Get a single random menu
@app.route('/api/menus', methods=['GET'])
def menus_list():
    try:
        results = es.search(index="menu", body={ "size": 1000 })

        return jsonify(results), 200
    except Exception as exception:
        return '{ "error": "Not Found" }', 404

# Get a single menu, by id
@app.route('/api/menu/<string:menu_id>', methods=['GET'])
def menu_single_id(menu_id):
    try:
        result = es.get(index="menu", doc_type='_doc', id=menu_id)

        return jsonify(result)
    except Exception as exception:
        return '{ "error": "Not Found" }', 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
