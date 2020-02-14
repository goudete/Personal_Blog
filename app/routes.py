from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/bookshelf')
def bookshelf():
    return render_template('bookshelf.html', title='Bookshelf')

@app.route('/laguide')
def laguide():
    return render_template('laguide.html', title='LA Guide')

@app.route('/thoughts')
def thoughts():
    return render_template('thoughts.html', title='Thoughts')

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')
