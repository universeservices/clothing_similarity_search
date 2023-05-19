import json
from flask import Flask, request, jsonify
from main import clothing_similarity_search

app = Flask(__name__)

@app.route('/clothing-similarity', methods=['POST'])
def clothing_similarity():
    data = request.get_json()

    input_text = data.get('input_text')
    top_n = data.get('top_n')

    results = clothing_similarity_search(input_text, top_n)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
