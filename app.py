from flask import Flask

# Create new flask app instance
app = Flask(__name__)

# Create root (starting point)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/')
def goodbye_world():
    return 'Goodbye World!'