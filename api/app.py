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
        results = es.search(index="menu", body={
            "query": {
                "function_score": {
                    "random_score": {
                        "seed": 10,
                        "field": "_seq_no"
                    }
                }
            },
            "size": 1000,
        })

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

# Get the current user's info
@app.route('/api/user', methods=['GET'])
def user_current():
    try:
        result = es.get(index="user", doc_type='_doc', id='a9bd0bd8-839b-11e9-8fc4-0242c0a82004')

        return jsonify(result), 200
    except Exception as exception:
        return '{ "error": "Not found" }', 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
