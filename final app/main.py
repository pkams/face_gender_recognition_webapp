from flask import Flask
from app import views, utils

app = Flask(__name__)

#urls
app.add_url_rule('/base', 'base', views.base)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/faceapp', 'faceapp', views.faceapp)
app.add_url_rule('/faceapp/gender', 'gender', views.gender, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)