from flask import Flask
import views

app =Flask(__name__)

# urls
app.add_url_rule('/', 'index', views.index, methods=['GET', 'POST'])
# run

if __name__ == '__main__':
    app.run(debug=True)