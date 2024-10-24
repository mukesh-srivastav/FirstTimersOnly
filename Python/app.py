from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_store = []

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Backend is up and running!"})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    data_store.append(data)
    return jsonify({"status": "Data added", "data": data_store}), 201

if __name__ == '__main__':
    app.run(debug=True)
