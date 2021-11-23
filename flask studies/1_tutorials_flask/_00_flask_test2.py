from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Testing web application'

@app.route('/route1')
def route1():
    return 'This is route1'

def route2():
    return 'This is another way to use routes!'

app.add_url_rule('/route2', 'route2', route2)

if __name__ == '__main__':
    app.run(debug=True)