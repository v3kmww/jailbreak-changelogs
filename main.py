from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
async def hello():
    with open('changelogs.txt', 'r') as f:
        return f.read()
    
# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
