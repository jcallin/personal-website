from flask import Flask, request, render_template
from content import Content

content_dict = Content()
app = Flask(__name__)

# Route the home directory of our webpage
@app.route('/')
def index():
    return render_template("main.html", content_dict = content_dict)

@app.errorhandler(404)
def page_not_found(e):
    return

# Only start the webserver if this file is called directly
if __name__ == "__main__":
    app.run(debug = True)