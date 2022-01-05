from os import name
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'title': 'Home',
        'heading' : 'Selamat datang di Home',
        'subheading': 'lorem ipsum'
    }
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    data = {
        'title': 'About',
        'heading' : 'About Us',
        'subheading': 'lorem ipsum'
    }
    return render_template('about.html',data=data)

@app.route('/blog')
def blog():
    data = {
        'title': 'Blog',
        'heading' : 'Blog',
        'subheading': 'lorem ipsum'
    }
    return render_template('blog/blog.html', data=data)


@app.route('/login')
def login():
    title = 'Login'
    return render_template('auth/login.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)