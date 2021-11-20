from flask import render_template, request

def index():
    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        email_id = request.form['email']
        print('first name = {} \n last name = {} \n email = {}'.format(first_name, last_name, email_id))
    return render_template('index.html')