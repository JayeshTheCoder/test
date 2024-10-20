from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/run_script', methods=['POST'])
def run_script():
    # Your script logic here
    return jsonify({"message": "Script run successfully"})

if __name__ == '__main__':
    app.run(debug=True)
