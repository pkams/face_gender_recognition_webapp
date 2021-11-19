from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Testing web application'

@app.route('/route1/<int:a>')
def route1(a):
    return f'This is route1 with number {a}'

@app.route('/weigth/<float:b>')
def route2(b):
    return f'This is weigth and your weigth is {b}'

if __name__ == '__main__':
    app.run(debug=True)