from flask import Flask, render_template, redirect, url_for, request
import os
from PIL import Image
from app.utils import predict_gender

UPLOAD_FOLDER = 'static/uploads/'

# Render templates

def base():
    return render_template('base.html')

def index():
    return render_template('index.html')

def faceapp():
    return render_template('faceapp.html')

def gender():
    if request.method == 'POST':
        f = request.files['image']
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        w = getproportion(path)
        print('File saved sucessfully in \n', path)
        predict_gender(path, f.filename)
        return render_template('genderapp.html', upload=True, fname=f.filename, w=w*300)

    return render_template('genderapp.html', upload=False)

# Extra functions
def getproportion(path):
    im = Image.open(path)
    w,h = im.size
    proportion = w/h
    return proportion
