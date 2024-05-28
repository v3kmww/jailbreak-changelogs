from flask import Flask
import requests
import os


# Create a Flask application
app = Flask(__name__)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            return response.json()['ip']
        else:
            return 'Unable to fetch public IP'
    except Exception as e:
        return f'Error: {e}'


# Define a route for the root URL
@app.route('/')
async def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    server_ip = get_public_ip()
    print(f'Hello, World! The server public IP address is {server_ip}')
    app.run(debug=True)
