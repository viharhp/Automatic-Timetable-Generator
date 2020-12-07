from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db'
db = SQLAlchemy(app)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(40), nullable=False)
    sub_code = db.Column(db.Integer, nullable=False)
    sub_sem = db.Column(db.Integer, nullable=False)
    sub_credits = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str(self.id)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(40), nullable=False)
    faculty_hours = db.Column(db.Integer, nullable=False)
    faculty_subject1 = db.Column(db.String(40), default='N/A')
    faculty_subject2 = db.Column(db.String(40), default='N/A')
    faculty_subject3 = db.Column(db.String(40), default='N/A')
    faculty_subject4 = db.Column(db.String(40), default='N/A')
    faculty_subject5 = db.Column(db.String(40), default='N/A')
    faculty_subject6 = db.Column(db.String(40), default='N/A')
    faculty_subject7 = db.Column(db.String(40), default='N/A')

    def __repr__(self):
        # returns id as default name of row
        return str("Subject" + self.id)

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_type = db.Column(db.String(40), nullable=False)
    class_number = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str("Subject" + self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/add-subject', methods=['GET','POST'])
def add_sub():
    if request.method == "POST":
        sub_sem = request.form.get('choosesemester')
        sub_name = request.form['subjectname']
        sub_code = request.form['subjectcode']
        sub_credits = request.form['subjectcredits']
        new_subject = Subject(sub_sem=sub_sem, sub_name=sub_name, sub_code=sub_code, sub_credits=sub_credits)
        db.session.add(new_subject) # added for this session only
        db.session.commit() # added permanently
        return redirect('/add-subject')
    else:
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
