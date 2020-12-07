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
    faculty_id = db.Column(db.Integer, primary_key=True)
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
        return str(self.faculty_id)

class Classroom(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    class_type = db.Column(db.String(40), nullable=False)
    class_number = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return str(self.class_id)

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
        all_subjects = Subject.query.order_by(Subject.id).all()
        return render_template('add-subject.html', subjects = all_subjects)
        # defined subjects variable which stores all_subjects, which we will use in drop down menu

@app.route('/add-classroom', methods=['GET','POST'])
def add_classroom():
    if request.method == "POST":
        class_type = request.form.get('classroomtype')
        class_number = request.form['class_number']
        new_class = Classroom(class_type=class_type, class_number=class_number)
        db.session.add(new_class) # added for this session only
        db.session.commit() # added permanently
        return redirect('/add-classroom')
    else:
        return render_template('add-classroom.html')

@app.route('/add-faculty', methods=['GET','POST'])
def add_faculty():
    if request.method == "POST":
        faculty_name = request.form['faculty_name']
        faculty_hours = request.form['faculty_hours']
        faculty_subject = request.form.get('faculty_subject')
        new_faculty = Faculty(faculty_name=faculty_name, faculty_hours=faculty_hours, faculty_subject1=faculty_subject)
        db.session.add(new_faculty) # added for this session only
        db.session.commit() # added permanently
        return redirect('/add-faculty')
    else:
        all_subjects = Subject.query.order_by(Subject.id).all()
        return render_template('add-faculty.html', subjects = all_subjects)

@app.route('/generate')
def generate():
        return render_template('generate.html')

@app.route('/view')
def view():
        return render_template('view.html')

if __name__ == '__main__':
    app.run(debug=True)
