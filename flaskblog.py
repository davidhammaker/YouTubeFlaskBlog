from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/about')
def about():
    return "What are you talking about?"


if __name__ == '__main__':
    app.run(debug=True)
