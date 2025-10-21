import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/health')
def health():
    return jsonify({"status": "OK", "message": "Scrideo is live!"})

@app.route('/demo')
def demo():
    return jsonify({
        "features": [
            "Video transcription",
            "YouTube processing", 
            "User authentication",
            "Caption customization",
            "History & favorites"
        ],
        "status": "ready"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
