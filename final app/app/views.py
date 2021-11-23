from flask import Flask, render_template, redirect, url_for

def base():
    return render_template('base.html')

def index():
    return render_template('index.html')

def faceapp():
    return render_template('faceapp.html')