# api/app.py

from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from random import randint

es = Elasticsearch(['http://elasticsearch:9200'])
app = Flask(__name__)

# Get a single random menu
@app.route('/api/menu/proposal', methods=['GET'])
def menu_single_proposal():
    results = es.search(index="menu")
    count = len(results['hits']['hits'])
    index = randint(0, count - 1)

    return jsonify(results['hits']['hits'][index]), 200

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
