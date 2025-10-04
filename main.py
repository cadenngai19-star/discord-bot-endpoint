from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/interactions', methods=['POST'])
def interactions():
    data = request.json
    if data['type'] == 1:
        return jsonify({"type": 1})
    return jsonify({
        "type": 4,
        "data": {
            "content": "Hello from Nevera!"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
