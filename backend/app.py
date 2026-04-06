# Import Flask framework and JSON response utility
from flask import Flask
from routes.items import items_bp

# Create Flask application instance
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(items_bp)

# Home route to check if server is running
@app.route('/')
def home():
    return "Resale System Running"

# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True) # Run server in debug mode(auto reload + error Logs)