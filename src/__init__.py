from flask import Flask

# __name__ is the name of the current file.
# Turn this file into a flask application
app = Flask(__name__)

import src.views
