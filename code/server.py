from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

word_list = ["apple", "banana", "cat"]  # 👈 You can change this
results = []

@app.route('/get-words', methods=['GET'])
def get_words():
    return jsonify(word_list)

@app.route('/post-result', methods=['POST'])
def post_result():
    data = request.json
    results.append(data)
    print("Received result:", data)
    return jsonify({"status": "success"})

@app.route('/get-results', methods=['GET'])
def get_results():
    return jsonify(results)

if _name_ == '_main_':
    app.run(debug=True, port=500)
