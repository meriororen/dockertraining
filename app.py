import os
from flask import Flask, render_template

app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route('/')
def index():
    return """
        <html><body style='background-color: {};'>
        <h1>Hello, World!</h1></body></html>""".format(color)

if __name__ == '__main__':
    app.run()
