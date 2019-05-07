# api/app.py

from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elasticsearch:9200'])
app = Flask(__name__)

@app.route('/api/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return '{ "method": "POST", "result": 200 }'
    else:
        results = es.indices.get_alias("*")
        return jsonify(results)

# Get a single random menu
@app.route('/api/menu/proposal', methods=['GET'])
def menu_single_proposal():
    return '{ "menu": { "name": "Gnocchis" } }'

# Get a single menu, by id
@app.route('/api/menu/<int:menu_id>', methods=['GET'])
def menu_single_id(menu_id):
    return '{ "menu": { "name": "Gnocchis (id: #%s)" } }' % menu_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
