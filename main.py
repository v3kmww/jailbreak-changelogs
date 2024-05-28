from flask import Flask
import os


# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
async def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    print(os.system('nmcli dev show eth0'))
    app.run(debug=True)
