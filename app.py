from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/detect', methods=['POST'])
def detect():
    # Ensure the request contains the 'text' key
    if 'text' not in request.json:
        return jsonify({"error": "Aucun texte fourni"}), 400

    text = request.json['text']
    try:
        # Call the ML model on port 6002
        response = requests.post('http://127.0.0.1:6002/detect', json={'text': text})
        
        if response.status_code == 200:
            language = response.json().get('language')
            return jsonify({"language": language})
        else:
            return jsonify({"error": "Erreur dans le modèle ML"}), 500

    except Exception as e:
        # Handle any exception during the connection or processing
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
