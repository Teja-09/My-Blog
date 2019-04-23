from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Miguel'}
    posts = [
        {
            'author': {'username': ' Teja'},
            'body': 'Smarter U Be'

        },

        {
            'author' : {'username': 'Ram'},
            'body' : 'I ejaculate Fire'
        }              
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)