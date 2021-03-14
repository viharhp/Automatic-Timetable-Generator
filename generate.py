import random
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db, Subject, Monday, Tuesday, Wednesday, Thursday, Friday, Faculty, Classroom

monday_subjects = Monday.query.order_by(Monday.m_id).all()
tuesday_subjects = Tuesday.query.order_by(Tuesday.t_id).all()
wednesday_subjects = Wednesday.query.order_by(Wednesday.w_id).all()
thursday_subjects = Thursday.query.order_by(Thursday.th_id).all()
friday_subjects = Friday.query.order_by(Friday.f_id).all()

all_faculty = Faculty.query.order_by(Faculty.faculty_id).all()
all_subjects = Subject.query.order_by(Subject.id).all()
all_class = Classroom.query.order_by(Classroom.class_id).all()

# subject list sem wise
sublist_sem3 = []
subcredits_sem3 = []
sublab_sem3 = []

sublist_sem5 = []
subcredits_sem5 = []
sublab_sem5 = []

sublist_sem7 = []
subcredits_sem7 = []
sublab_sem7 = []

#faculty list subject wise
faculty_list = []
for faculty in all_faculty:
    faculty_list.append(faculty.faculty_name)

#class list class wise
class_lab = []
class_lecture = []

for classes in all_class:
    if classes.class_type == 'lab':
        class_lab.append(classes.class_number)
    elif classes.class_type == 'lecture':
        class_lecture.append(classes.class_number)
    else:
        break

for subject in all_subjects:
    if subject.sub_sem == 3:
        sublist_sem3.append(subject.sub_name)
        subcredits_sem3.append(subject.sub_credits)
        sublab_sem3.append(subject.is_lab)
    elif subject.sub_sem == 5:
        sublist_sem5.append(subject.sub_name)
        subcredits_sem5.append(subject.sub_credits)
        sublab_sem5.append(subject.is_lab)
    elif subject.sub_sem == 7:
        sublist_sem7.append(subject.sub_name)
        subcredits_sem7.append(subject.sub_credits)
        sublab_sem7.append(subject.is_lab)
    else:
        break
'''
print(len(sublist_sem3)) # to find length of list
print(sublist_sem3)
print(subcredits_sem3)
print(sublab_sem3)

print(sublist_sem5)
print(subcredits_sem5)
print(sublab_sem5)

print(sublist_sem7)
print(subcredits_sem7)
print(sublab_sem7)
'''
def timetable():
    for monday_subject in monday_subjects:
        sub_random = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        if monday_subject.asubject3 == 'none':
            monday_subject.asubject3 = sublist_sem3[sub_random]
            monday_subject.aclass3 = class_lecture[lec_random]
            monday_subject.afaculty3 = faculty_list[fac_random]
            print(sublist_sem3[sub_random] + ' ' + class_lecture[lec_random] + ' ' + faculty_list[fac_random])
            db.session.commit()
timetable()

'''
def start():
        all_subjects = Subject.query.order_by(Subject.id).all()
        # qyerying all subjects
        for subject in all_subjects:
        # checking semester of subject
            if subject.sub_sem == 3:
                # verifying subject has lab or not
                if subject.is_lab == 1:
                    # rnumber = random.randint(0,5)
                    for monday_subject in monday_subjects:
                        if monday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            #monday_subject.aclass3 = class1
                            #monday_subject.afaculty3 = fac1
                            monday_subject.asubject3 = subject.sub_name
                            db.session.commit()

                    for tuesday_subject in tuesday_subjects:
                        if tuesday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            tuesday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for wednesday_subject in wednesday_subjects:
                        if wednesday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            wednesday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for thursday_subject in thursday_subjects:
                        if thursday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            thursday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for friday_subject in friday_subjects:
                        if friday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            friday_subject.asubject3 = subject.sub_name
                            db.session.commit()
            elif subject.sub_sem == 5:
                # verifying subject has lab or not
                if subject.is_lab == 1:
                    # rnumber = random.randint(0,5)
                    for monday_subject in monday_subjects:
                        if monday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            monday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for tuesday_subject in tuesday_subjects:
                        if tuesday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            tuesday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for wednesday_subject in wednesday_subjects:
                        if wednesday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            wednesday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for thursday_subject in thursday_subjects:
                        if thursday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            thursday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for friday_subject in friday_subjects:
                        if friday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            friday_subject.asubject3 = subject.sub_name
                            db.session.commit()
            elif subject.sub_sem == 7:
                # verifying subject has lab or not
                if subject.is_lab == 1:
                    # rnumber = random.randint(0,5)
                    for monday_subject in monday_subjects:
                        if monday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            monday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for tuesday_subject in tuesday_subjects:
                        if tuesday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            tuesday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for wednesday_subject in wednesday_subjects:
                        if wednesday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            wednesday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for thursday_subject in thursday_subjects:
                        if thursday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            thursday_subject.asubject3 = subject.sub_name
                            db.session.commit()
                    for friday_subject in friday_subjects:
                        if friday_subject.asubject3 == 'none':
                            print(" Added " + subject.sub_name)
                            friday_subject.asubject3 = subject.sub_name
                            db.session.commit()
            else:
                break
start()
'''
'''
elif subject.sub_sem == 5:
    # verifying subject has lab or not
    if subject.is_lab == 1:
        # rnumber = random.randint(0,5)
        for monday_subject in monday_subjects:
            if monday_subject.asubject5 == 'none':
                print(" Added " + subject.sub_name)
                monday_subject.asubject5 = subject.sub_name
                db.session.commit()
            elif monday_subject.bsubject5 == 'none':
                print(" Added " + subject.sub_name)
                monday_subject.bsubject5 = subject.sub_name
                db.session.commit()
            elif monday_subject.csubject5 == 'none':
                print(" Added " + subject.sub_name)
                monday_subject.csubject5 = subject.sub_name
                db.session.commit()
    elif subject.sub_sem == 7:
        # verifying subject has lab or not
        if subject.is_lab == 1:
            # rnumber = random.randint(0,5)
            for monday_subject in monday_subjects:
                if monday_subject.asubject7 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.asubject7 = subject.sub_name
                    db.session.commit()
                elif monday_subject.bsubject7 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.bsubject7 = subject.sub_name
                    db.session.commit()
                elif monday_subject.csubject7 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.csubject7 = subject.sub_name
                    db.session.commit()
else:
    break
for monday_subject in monday_subjects:
    if monday_subject.asubject3 == 'none':
        print(" Added " + subject.sub_name)
        monday_subject.asubject3 = subject.sub_name
        db.session.commit()
    elif monday_subject.bsubject3 == 'none':
        print(" Added " + subject.sub_name)
        monday_subject.bsubject3 = subject.sub_name
        db.session.commit()
    elif monday_subject.csubject3 == 'none':
        print(" Added " + subject.sub_name)
        monday_subject.csubject3 = subject.sub_name
        db.session.commit()
'''
