from flask import Flask, request, jsonify
from backend.data_processor import process_data

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    query = request.args.to_dict()
    data = process_data(query)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
