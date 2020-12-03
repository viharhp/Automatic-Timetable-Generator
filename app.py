from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/add-subject')
def add_sub():
        return render_template('add-subject.html')

@app.route('/add-classroom')
def add_classroom():
        return render_template('add-classroom.html')

@app.route('/add-faculty')
def add_faculty():
        return render_template('add-faculty.html')

@app.route('/generate')
def generate():
        return render_template('generate.html')

@app.route('/view')
def view():
        return render_template('view.html')

if __name__ == '__main__':
    app.run(debug=True)
