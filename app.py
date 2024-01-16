from flask import Flask
from flask_ngrok2 import run_with_ngrok
app = Flask(__name__)

run_with_ngrok(app)
@app.route("/")
def welcome():
    return "avfcHedsalkllo"

@app.route("/home")
def home():
    return "myhokjme"


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)

from controllers import *
# import controllers.signup
# import controllers.products
# if __name__ == "__main__":
#     app.run(debug=True)