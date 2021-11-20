from flask import Flask
import views

app = Flask(__name__)

# Create rule(URL)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/templates/<name>/<int:marks>', 'index_template', views.index_tem)
app.add_url_rule('/template_for', 'template_for', views.index_tem_for)

# run the flask app

if __name__ == '__main__':
    app.run(debug=True)