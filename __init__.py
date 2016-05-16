from flask import Flask, request, render_template

app = Flask(__name__)

# Route the home directory of our webpage
@app.route('/')
def index():
    return render_template("main.html")

# Only start the webserver if this file is called directly
if __name__ == "__main__":
    app.run(debug = True)