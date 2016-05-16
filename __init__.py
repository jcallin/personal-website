from flask import Flask, request

app = Flask(__name__)

# Route the home directory of our webpage
@app.route('/')
def index():
    return 'This is the homepage'

# Only start the webserver if this file is called directly
if __name__ == "__main__":
    app.run(debug = True)