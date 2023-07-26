from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! modified for checking purpose, last modified.'

if __name__ == '__main__':
    app.run()

