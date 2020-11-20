
# flasblueprint encapsulates functionality eg. views and templates
from flask import Flask
from example_blueprint import example_blueprint

app= Flask(__name__)
app.register_blueprint(example_blueprint)

#@app.route('/')
#def index():
    #return "this is an example app"