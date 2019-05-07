# api/app.py

from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elasticsearch:9200'])
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    results = es.indices.get_alias("*")
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
