# Import Flask framework and JSON response utility
from flask import Flask, jsonify

# Create Flask application instance
app = Flask(__name__)

# Temporary in-memory storage (acts like a database)
items = []

# Home route to check if server is running
@app.route('/')
def home():
    return "Resale System Running"

# Route to get all items (READ operation)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items) # Convert Python list to JSON response

# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True) # Run server in debug mode(auto reload + error Logs)