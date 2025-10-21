from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

# Add these basic routes to stop 404 errors
@app.route('/profile', methods=['GET'])
def profile():
    return jsonify({"status": "feature_coming_soon", "message": "User profiles coming soon!"})

@app.route('/upload', methods=['POST'])
def upload():
    return jsonify({"status": "feature_coming_soon", "message": "File upload coming soon!"})

@app.route('/health')
def health():
    return jsonify({"status": "live", "message": "Scrideo is running!"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
