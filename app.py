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
    faculty_subject1 = db.Column(db.String(40), default='None')
    faculty_subject2 = db.Column(db.String(40), default='None')
    faculty_subject3 = db.Column(db.String(40), default='None')
    faculty_subject4 = db.Column(db.String(40), default='None')
    faculty_subject5 = db.Column(db.String(40), default='None')
    faculty_subject6 = db.Column(db.String(40), default='None')
    faculty_subject7 = db.Column(db.String(40), default='None')

    def __repr__(self):
        return str(self.faculty_id)

class Classroom(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    class_type = db.Column(db.String(40), nullable=False)
    class_number = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return str(self.class_id)

class Monday(db.Model):
    m_id = db.Column(db.Integer, primary_key=True)
    aclass3 = db.Column(db.String(40), nullable=False)
    afaculty3 = db.Column(db.String(40), nullable=False)
    asubject3 = db.Column(db.String(40), nullable=False)
    bclass3 = db.Column(db.String(40), nullable=False)
    bfaculty3 = db.Column(db.String(40), nullable=False)
    bsubject3 = db.Column(db.String(40), nullable=False)
    cclass3 = db.Column(db.String(40), nullable=False)
    cfaculty3 = db.Column(db.String(40), nullable=False)
    csubject3 = db.Column(db.String(40), nullable=False)

    aclass5 = db.Column(db.String(40), nullable=False)
    afaculty5 = db.Column(db.String(40), nullable=False)
    asubject5 = db.Column(db.String(40), nullable=False)
    bclass5= db.Column(db.String(40), nullable=False)
    bfaculty5= db.Column(db.String(40), nullable=False)
    bsubject5= db.Column(db.String(40), nullable=False)
    cclass5= db.Column(db.String(40), nullable=False)
    cfaculty5= db.Column(db.String(40), nullable=False)
    csubject5= db.Column(db.String(40), nullable=False)

    aclass7 = db.Column(db.String(40), nullable=False)
    afaculty7 = db.Column(db.String(40), nullable=False)
    asubject7 = db.Column(db.String(40), nullable=False)
    bclass7 = db.Column(db.String(40), nullable=False)
    bfaculty7 = db.Column(db.String(40), nullable=False)
    bsubject7 = db.Column(db.String(40), nullable=False)
    cclass7 = db.Column(db.String(40), nullable=False)
    cfaculty7 = db.Column(db.String(40), nullable=False)
    csubject7 = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str(self.m_id)

class Tuesday(db.Model):
    t_id = db.Column(db.Integer, primary_key=True)
    aclass3 = db.Column(db.String(40), nullable=False)
    afaculty3 = db.Column(db.String(40), nullable=False)
    asubject3 = db.Column(db.String(40), nullable=False)
    bclass3 = db.Column(db.String(40), nullable=False)
    bfaculty3 = db.Column(db.String(40), nullable=False)
    bsubject3 = db.Column(db.String(40), nullable=False)
    cclass3 = db.Column(db.String(40), nullable=False)
    cfaculty3 = db.Column(db.String(40), nullable=False)
    csubject3 = db.Column(db.String(40), nullable=False)

    aclass5 = db.Column(db.String(40), nullable=False)
    afaculty5 = db.Column(db.String(40), nullable=False)
    asubject5 = db.Column(db.String(40), nullable=False)
    bclass5= db.Column(db.String(40), nullable=False)
    bfaculty5= db.Column(db.String(40), nullable=False)
    bsubject5= db.Column(db.String(40), nullable=False)
    cclass5= db.Column(db.String(40), nullable=False)
    cfaculty5= db.Column(db.String(40), nullable=False)
    csubject5= db.Column(db.String(40), nullable=False)

    aclass7 = db.Column(db.String(40), nullable=False)
    afaculty7 = db.Column(db.String(40), nullable=False)
    asubject7 = db.Column(db.String(40), nullable=False)
    bclass7 = db.Column(db.String(40), nullable=False)
    bfaculty7 = db.Column(db.String(40), nullable=False)
    bsubject7 = db.Column(db.String(40), nullable=False)
    cclass7 = db.Column(db.String(40), nullable=False)
    cfaculty7 = db.Column(db.String(40), nullable=False)
    csubject7 = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str(self.t_id)

class Wednesday(db.Model):
    w_id = db.Column(db.Integer, primary_key=True)
    aclass3 = db.Column(db.String(40), nullable=False)
    afaculty3 = db.Column(db.String(40), nullable=False)
    asubject3 = db.Column(db.String(40), nullable=False)
    bclass3 = db.Column(db.String(40), nullable=False)
    bfaculty3 = db.Column(db.String(40), nullable=False)
    bsubject3 = db.Column(db.String(40), nullable=False)
    cclass3 = db.Column(db.String(40), nullable=False)
    cfaculty3 = db.Column(db.String(40), nullable=False)
    csubject3 = db.Column(db.String(40), nullable=False)

    aclass5 = db.Column(db.String(40), nullable=False)
    afaculty5 = db.Column(db.String(40), nullable=False)
    asubject5 = db.Column(db.String(40), nullable=False)
    bclass5= db.Column(db.String(40), nullable=False)
    bfaculty5= db.Column(db.String(40), nullable=False)
    bsubject5= db.Column(db.String(40), nullable=False)
    cclass5= db.Column(db.String(40), nullable=False)
    cfaculty5= db.Column(db.String(40), nullable=False)
    csubject5= db.Column(db.String(40), nullable=False)

    aclass7 = db.Column(db.String(40), nullable=False)
    afaculty7 = db.Column(db.String(40), nullable=False)
    asubject7 = db.Column(db.String(40), nullable=False)
    bclass7 = db.Column(db.String(40), nullable=False)
    bfaculty7 = db.Column(db.String(40), nullable=False)
    bsubject7 = db.Column(db.String(40), nullable=False)
    cclass7 = db.Column(db.String(40), nullable=False)
    cfaculty7 = db.Column(db.String(40), nullable=False)
    csubject7 = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str(self.w_id)

class Thursday(db.Model):
    th_id = db.Column(db.Integer, primary_key=True)
    aclass3 = db.Column(db.String(40), nullable=False)
    afaculty3 = db.Column(db.String(40), nullable=False)
    asubject3 = db.Column(db.String(40), nullable=False)
    bclass3 = db.Column(db.String(40), nullable=False)
    bfaculty3 = db.Column(db.String(40), nullable=False)
    bsubject3 = db.Column(db.String(40), nullable=False)
    cclass3 = db.Column(db.String(40), nullable=False)
    cfaculty3 = db.Column(db.String(40), nullable=False)
    csubject3 = db.Column(db.String(40), nullable=False)

    aclass5 = db.Column(db.String(40), nullable=False)
    afaculty5 = db.Column(db.String(40), nullable=False)
    asubject5 = db.Column(db.String(40), nullable=False)
    bclass5= db.Column(db.String(40), nullable=False)
    bfaculty5= db.Column(db.String(40), nullable=False)
    bsubject5= db.Column(db.String(40), nullable=False)
    cclass5= db.Column(db.String(40), nullable=False)
    cfaculty5= db.Column(db.String(40), nullable=False)
    csubject5= db.Column(db.String(40), nullable=False)

    aclass7 = db.Column(db.String(40), nullable=False)
    afaculty7 = db.Column(db.String(40), nullable=False)
    asubject7 = db.Column(db.String(40), nullable=False)
    bclass7 = db.Column(db.String(40), nullable=False)
    bfaculty7 = db.Column(db.String(40), nullable=False)
    bsubject7 = db.Column(db.String(40), nullable=False)
    cclass7 = db.Column(db.String(40), nullable=False)
    cfaculty7 = db.Column(db.String(40), nullable=False)
    csubject7 = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str(self.th_id)

class Friday(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    aclass3 = db.Column(db.String(40), nullable=False)
    afaculty3 = db.Column(db.String(40), nullable=False)
    asubject3 = db.Column(db.String(40), nullable=False)
    bclass3 = db.Column(db.String(40), nullable=False)
    bfaculty3 = db.Column(db.String(40), nullable=False)
    bsubject3 = db.Column(db.String(40), nullable=False)
    cclass3 = db.Column(db.String(40), nullable=False)
    cfaculty3 = db.Column(db.String(40), nullable=False)
    csubject3 = db.Column(db.String(40), nullable=False)

    aclass5 = db.Column(db.String(40), nullable=False)
    afaculty5 = db.Column(db.String(40), nullable=False)
    asubject5 = db.Column(db.String(40), nullable=False)
    bclass5= db.Column(db.String(40), nullable=False)
    bfaculty5= db.Column(db.String(40), nullable=False)
    bsubject5= db.Column(db.String(40), nullable=False)
    cclass5= db.Column(db.String(40), nullable=False)
    cfaculty5= db.Column(db.String(40), nullable=False)
    csubject5= db.Column(db.String(40), nullable=False)

    aclass7 = db.Column(db.String(40), nullable=False)
    afaculty7 = db.Column(db.String(40), nullable=False)
    asubject7 = db.Column(db.String(40), nullable=False)
    bclass7 = db.Column(db.String(40), nullable=False)
    bfaculty7 = db.Column(db.String(40), nullable=False)
    bsubject7 = db.Column(db.String(40), nullable=False)
    cclass7 = db.Column(db.String(40), nullable=False)
    cfaculty7 = db.Column(db.String(40), nullable=False)
    csubject7 = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # returns id as default name of row
        return str(self.f_id)

class Time(db.Model):
    time_id = db.Column(db.Integer, primary_key=True)
    lec1 = db.Column(db.String(10), nullable=False, default='09:15')
    lec2 = db.Column(db.String(10), nullable=False, default='10:15')
    lec3 = db.Column(db.String(10), nullable=False, default='11:45')
    lec4 = db.Column(db.String(10), nullable=False, default='12:45')
    lec5 = db.Column(db.String(10), nullable=False, default='14:00')
    lec6 = db.Column(db.String(10), nullable=False, default='15:00')
    end_time = db.Column(db.String(10), nullable=False, default='11:15')
    recess1 = db.Column(db.String(10), nullable=False, default='13:45')
    recess2 = db.Column(db.String(10), nullable=False, default='16:00')
    def __repr__(self):
        # returns id as default name of row
        return str(self.time_id)

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
        all_subject = Subject.query.order_by(Subject.id).all()
        return render_template('add-subject.html', subjects = all_subject)
        # defined subjects variable which stores all_subjects, which we will use in drop down menu

@app.route('/edit/subject/<int:id>', methods=['GET','POST'])
def edit_subject(id):
    subject = Subject.query.get_or_404(id)
    if request.method == "POST":
        subject.sub_sem = request.form.get('choosesemester')
        subject.sub_name = request.form['subjectname']
        subject.sub_code = request.form['subjectcode']
        subject.sub_credits = request.form['subjectcredits']
        db.session.commit() # added permanently
        return redirect('/add-subject')
    else:
        return render_template('edit-subject.html', subject = subject)

@app.route('/delete/subject/<int:id>', methods=['GET','DELETE'])
def delete_subject(id):
    del_subject = Subject.query.get_or_404(id)
    db.session.delete(del_subject)
    db.session.commit()
    return redirect('/add-subject')

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
        all_classroom = Classroom.query.order_by(Classroom.class_id).all()
        return render_template('add-classroom.html', classrooms = all_classroom) # to use in loops

@app.route('/edit/classroom/<int:id>', methods=['GET','POST','DELETE'])
def edit_classroom(id):
    classroom = Classroom.query.get_or_404(id)
    if request.method == "POST":
        classroom.class_type = request.form.get('classroomtype')
        classroom.class_number = request.form['class_number']
        db.session.commit() # added permanently
        return redirect('/add-classroom')
    else:
        return render_template('edit-classroom.html', classroom = classroom)

@app.route('/delete/classroom/<int:id>', methods=['GET','DELETE'])
def delete_classroom(id):
    del_classroom = Classroom.query.get_or_404(id)
    db.session.delete(del_classroom)
    db.session.commit()
    return redirect('/add-classroom')

@app.route('/add-faculty', methods=['GET','POST'])
def add_faculty():
    if request.method == "POST":
        faculty_name = request.form['faculty_name']
        faculty_hours = request.form['faculty_hours']
        faculty_subject1 = request.form.get('faculty_subject1')
        faculty_subject2 = request.form.get('faculty_subject2')
        faculty_subject3 = request.form.get('faculty_subject3')
        faculty_subject4 = request.form.get('faculty_subject4')
        faculty_subject5 = request.form.get('faculty_subject5')
        faculty_subject6 = request.form.get('faculty_subject6')
        faculty_subject7 = request.form.get('faculty_subject7')
        new_faculty = Faculty(faculty_name=faculty_name, faculty_hours=faculty_hours, faculty_subject1=faculty_subject1, faculty_subject2=faculty_subject2, faculty_subject3=faculty_subject3, faculty_subject4=faculty_subject4, faculty_subject5=faculty_subject5, faculty_subject6=faculty_subject6, faculty_subject7=faculty_subject7)
        db.session.add(new_faculty) # added for this session only
        db.session.commit() # added permanently
        return redirect('/add-faculty')
    else:
        all_faculties = Faculty.query.order_by(Faculty.faculty_id).all()
        all_subjects = Subject.query.order_by(Subject.id).all()
        return render_template('add-faculty.html', subjects = all_subjects, faculties = all_faculties) # to use in loops

@app.route('/edit/faculty/<int:id>', methods=['GET','POST'])
def edit_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    if request.method == "POST":
        faculty.faculty_name = request.form['faculty_name']
        faculty.faculty_hours = request.form['faculty_hours']
        faculty.faculty_subject1 = request.form['faculty_subject1']
        faculty.faculty_subject2 = request.form['faculty_subject2']
        faculty.faculty_subject3 = request.form['faculty_subject3']
        faculty.faculty_subject4 = request.form['faculty_subject4']
        faculty.faculty_subject5 = request.form['faculty_subject5']
        faculty.faculty_subject6 = request.form['faculty_subject6']
        faculty.faculty_subject7 = request.form['faculty_subject7']
        db.session.commit() # added permanently
        return redirect('/add-faculty')
    else:
        subjects = Subject.query.order_by(Subject.id).all()
        return render_template('edit-faculty.html', faculty = faculty, subjects = subjects)


@app.route('/delete/faculty/<int:id>', methods=['GET','DELETE'])
def delete_faculty(id):
    del_faculty = Faculty.query.get_or_404(id)
    db.session.delete(del_faculty)
    db.session.commit()
    return redirect('/add-faculty')

@app.route('/set-time', methods=['GET','POST'])
def set_time():
    if request.method == "POST":
        lec1 = request.form.get('lec1')
        lec2 = request.form.get('lec2')
        lec3 = request.form.get('lec3')
        lec4 = request.form.get('lec4')
        lec5 = request.form.get('lec5')
        lec6 = request.form.get('lec6')
        end_time = request.form.get('end_time')
        recess1 = request.form.get('recess1')
        recess2 = request.form.get('recess2')

        newtime = Time(lec1 = lec1, lec2 = lec2, lec3 = lec3, lec4 = lec4, lec5 = lec5, lec6 = lec6, recess1 = recess1, recess2 = recess2, end_time = end_time)
        db.session.add(newtime)
        db.session.commit()
        return redirect('/set-time')
    else:
        return render_template('set-time.html')

@app.route('/drop-table', methods=['GET','DELETE'])
def drop_table(id):
    del_faculty = Faculty.query.get_or_404(id)
    db.session.delete(del_faculty)
    db.session.commit()
    return redirect('/add-faculty')

@app.route('/generate', methods=['GET','POST'])
def generate():
        timing = Time.query.order_by(Time.time_id).all()
        monday_subjects = Monday.query.order_by(Monday.m_id).all()
        tuesday_subjects = Tuesday.query.order_by(Tuesday.t_id).all()
        wednesday_subjects = Wednesday.query.order_by(Wednesday.w_id).all()
        thursday_subjects = Thursday.query.order_by(Thursday.th_id).all()
        friday_subjects = Friday.query.order_by(Friday.f_id).all()
        return render_template('generate.html', mondays = monday_subjects, tuesdays = tuesday_subjects, wednesdays = wednesday_subjects , thursdays = thursday_subjects, fridays = friday_subjects, times = timing)

@app.route('/view')
def view():
        return render_template('view.html')

if __name__ == '__main__':
    # db.create.all()
    app.run(debug=True)
