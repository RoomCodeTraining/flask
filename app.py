import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get('PORT', 5000))
