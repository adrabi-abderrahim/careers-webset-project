from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellp_app():
  return '<h1>Hello App</h1>'