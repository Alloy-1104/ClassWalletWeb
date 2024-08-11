from flask import Flask
app = Flask(__name__)

from cww.views import *
import cww.models

if __name__ == "__main__":
    app.run(debug=True)