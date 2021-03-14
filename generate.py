import random
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db, Subject, Monday, Tuesday, Wednesday, Thursday, Friday, Faculty, Classroom


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


    for monday_subject in monday_subjects:
        sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
        sub_random7 = random.randint(0,len(sublist_sem7)-1)
        if monday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # subject assigning for 3a-3b-3c
            monday_subject.asubject3 = sublist_sem3[sub_random3]
            monday_subject.aclass3 = class_lecture[lec_random]
            monday_subject.afaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            monday_subject.bsubject3 = sublist_sem3[sub_random3]
            monday_subject.bclass3 = class_lecture[lec_random]
            monday_subject.bfaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            monday_subject.csubject3 = sublist_sem3[sub_random3]
            monday_subject.cclass3 = class_lecture[lec_random]
            monday_subject.cfaculty3 = faculty_list[fac_random]

            # ----------------------SEM - 5 -----------------------
            monday_subject.asubject5 = sublist_sem3[sub_random5]
            monday_subject.aclass5 = class_lecture[lec_random]
            monday_subject.afaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            monday_subject.bsubject5 = sublist_sem5[sub_random5]
            monday_subject.bclass5 = class_lecture[lec_random]
            monday_subject.bfaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            monday_subject.csubject5 = sublist_sem5[sub_random5]
            monday_subject.cclass5 = class_lecture[lec_random]
            monday_subject.cfaculty5 = faculty_list[fac_random]

            # ----------------------SEM - 7 -----------------------
            monday_subject.asubject7 = sublist_sem3[sub_random7]
            monday_subject.aclass7 = class_lecture[lec_random]
            monday_subject.afaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            monday_subject.bsubject7 = sublist_sem7[sub_random7]
            monday_subject.bclass7 = class_lecture[lec_random]
            monday_subject.bfaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            monday_subject.csubject7 = sublist_sem7[sub_random7]
            monday_subject.cclass7 = class_lecture[lec_random]
            monday_subject.cfaculty7 = faculty_list[fac_random]

            print(sublist_sem3[sub_random3] + ' ' + class_lecture[lec_random] + ' ' + faculty_list[fac_random])
            db.session.commit()
    for tuesday_subject in tuesday_subjects:
        sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
        sub_random7 = random.randint(0,len(sublist_sem7)-1)
        if tuesday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # subject assigning for 3a-3b-3c
            tuesday_subject.asubject3 = sublist_sem3[sub_random3]
            tuesday_subject.aclass3 = class_lecture[lec_random]
            tuesday_subject.afaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            tuesday_subject.bsubject3 = sublist_sem3[sub_random3]
            tuesday_subject.bclass3 = class_lecture[lec_random]
            tuesday_subject.bfaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            tuesday_subject.csubject3 = sublist_sem3[sub_random3]
            tuesday_subject.cclass3 = class_lecture[lec_random]
            tuesday_subject.cfaculty3 = faculty_list[fac_random]

            # ----------------------SEM - 5 -----------------------
            tuesday_subject.asubject5 = sublist_sem3[sub_random5]
            tuesday_subject.aclass5 = class_lecture[lec_random]
            tuesday_subject.afaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            tuesday_subject.bsubject5 = sublist_sem5[sub_random5]
            tuesday_subject.bclass5 = class_lecture[lec_random]
            tuesday_subject.bfaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            tuesday_subject.csubject5 = sublist_sem5[sub_random5]
            tuesday_subject.cclass5 = class_lecture[lec_random]
            tuesday_subject.cfaculty5 = faculty_list[fac_random]

            # ----------------------SEM - 7 -----------------------
            tuesday_subject.asubject7 = sublist_sem3[sub_random7]
            tuesday_subject.aclass7 = class_lecture[lec_random]
            tuesday_subject.afaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            tuesday_subject.bsubject7 = sublist_sem7[sub_random7]
            tuesday_subject.bclass7 = class_lecture[lec_random]
            tuesday_subject.bfaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            tuesday_subject.csubject7 = sublist_sem7[sub_random7]
            tuesday_subject.cclass7 = class_lecture[lec_random]
            tuesday_subject.cfaculty7 = faculty_list[fac_random]
            db.session.commit()
    for wednesday_subject in wednesday_subjects:
        sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
        sub_random7 = random.randint(0,len(sublist_sem7)-1)
        if wednesday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # subject assigning for 3a-3b-3c
            wednesday_subject.asubject3 = sublist_sem3[sub_random3]
            wednesday_subject.aclass3 = class_lecture[lec_random]
            wednesday_subject.afaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            wednesday_subject.bsubject3 = sublist_sem3[sub_random3]
            wednesday_subject.bclass3 = class_lecture[lec_random]
            wednesday_subject.bfaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            wednesday_subject.csubject3 = sublist_sem3[sub_random3]
            wednesday_subject.cclass3 = class_lecture[lec_random]
            wednesday_subject.cfaculty3 = faculty_list[fac_random]

            # ----------------------SEM - 5 -----------------------
            wednesday_subject.asubject5 = sublist_sem3[sub_random5]
            wednesday_subject.aclass5 = class_lecture[lec_random]
            wednesday_subject.afaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            wednesday_subject.bsubject5 = sublist_sem5[sub_random5]
            wednesday_subject.bclass5 = class_lecture[lec_random]
            wednesday_subject.bfaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            wednesday_subject.csubject5 = sublist_sem5[sub_random5]
            wednesday_subject.cclass5 = class_lecture[lec_random]
            wednesday_subject.cfaculty5 = faculty_list[fac_random]

            # ----------------------SEM - 7 -----------------------
            wednesday_subject.asubject7 = sublist_sem3[sub_random7]
            wednesday_subject.aclass7 = class_lecture[lec_random]
            wednesday_subject.afaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            wednesday_subject.bsubject7 = sublist_sem7[sub_random7]
            wednesday_subject.bclass7 = class_lecture[lec_random]
            wednesday_subject.bfaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            wednesday_subject.csubject7 = sublist_sem7[sub_random7]
            wednesday_subject.cclass7 = class_lecture[lec_random]
            wednesday_subject.cfaculty7 = faculty_list[fac_random]

            print(sublist_sem3[sub_random3] + ' ' + class_lecture[lec_random] + ' ' + faculty_list[fac_random])
            db.session.commit()

    for thursday_subject in thursday_subjects:
        sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
        sub_random7 = random.randint(0,len(sublist_sem7)-1)
        if thursday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # subject assigning for 3a-3b-3c
            thursday_subject.asubject3 = sublist_sem3[sub_random3]
            thursday_subject.aclass3 = class_lecture[lec_random]
            thursday_subject.afaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            thursday_subject.bsubject3 = sublist_sem3[sub_random3]
            thursday_subject.bclass3 = class_lecture[lec_random]
            thursday_subject.bfaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            thursday_subject.csubject3 = sublist_sem3[sub_random3]
            thursday_subject.cclass3 = class_lecture[lec_random]
            thursday_subject.cfaculty3 = faculty_list[fac_random]

            # ----------------------SEM - 5 -----------------------
            thursday_subject.asubject5 = sublist_sem3[sub_random5]
            thursday_subject.aclass5 = class_lecture[lec_random]
            thursday_subject.afaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            thursday_subject.bsubject5 = sublist_sem5[sub_random5]
            thursday_subject.bclass5 = class_lecture[lec_random]
            thursday_subject.bfaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            thursday_subject.csubject5 = sublist_sem5[sub_random5]
            thursday_subject.cclass5 = class_lecture[lec_random]
            thursday_subject.cfaculty5 = faculty_list[fac_random]

            # ----------------------SEM - 7 -----------------------
            thursday_subject.asubject7 = sublist_sem3[sub_random7]
            thursday_subject.aclass7 = class_lecture[lec_random]
            thursday_subject.afaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            thursday_subject.bsubject7 = sublist_sem7[sub_random7]
            thursday_subject.bclass7 = class_lecture[lec_random]
            thursday_subject.bfaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            thursday_subject.csubject7 = sublist_sem7[sub_random7]
            thursday_subject.cclass7 = class_lecture[lec_random]
            thursday_subject.cfaculty7 = faculty_list[fac_random]

            print(sublist_sem3[sub_random3] + ' ' + class_lecture[lec_random] + ' ' + faculty_list[fac_random])
            db.session.commit()
    for friday_subject in friday_subjects:
        sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
        sub_random7 = random.randint(0,len(sublist_sem7)-1)
        if friday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # subject assigning for 3a-3b-3c
            friday_subject.asubject3 = sublist_sem3[sub_random3]
            friday_subject.aclass3 = class_lecture[lec_random]
            friday_subject.afaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            friday_subject.bsubject3 = sublist_sem3[sub_random3]
            friday_subject.bclass3 = class_lecture[lec_random]
            friday_subject.bfaculty3 = faculty_list[fac_random]
            sub_random3 = random.randint(0,len(sublist_sem3)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            friday_subject.csubject3 = sublist_sem3[sub_random3]
            friday_subject.cclass3 = class_lecture[lec_random]
            friday_subject.cfaculty3 = faculty_list[fac_random]

            # ----------------------SEM - 5 -----------------------
            friday_subject.asubject5 = sublist_sem3[sub_random5]
            friday_subject.aclass5 = class_lecture[lec_random]
            friday_subject.afaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            friday_subject.bsubject5 = sublist_sem5[sub_random5]
            friday_subject.bclass5 = class_lecture[lec_random]
            friday_subject.bfaculty5 = faculty_list[fac_random]
            sub_random5 = random.randint(0,len(sublist_sem5)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            friday_subject.csubject5 = sublist_sem5[sub_random5]
            friday_subject.cclass5 = class_lecture[lec_random]
            friday_subject.cfaculty5 = faculty_list[fac_random]

            # ----------------------SEM - 7 -----------------------
            friday_subject.asubject7 = sublist_sem3[sub_random7]
            friday_subject.aclass7 = class_lecture[lec_random]
            friday_subject.afaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            friday_subject.bsubject7 = sublist_sem7[sub_random7]
            friday_subject.bclass7 = class_lecture[lec_random]
            friday_subject.bfaculty7 = faculty_list[fac_random]
            sub_random7 = random.randint(0,len(sublist_sem7)-1) # length starts from 1 but list starts from 0 thus minus 1
            lab_random = random.randint(0,len(class_lab)-1)
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)
            friday_subject.csubject7 = sublist_sem7[sub_random7]
            friday_subject.cclass7 = class_lecture[lec_random]
            friday_subject.cfaculty7 = faculty_list[fac_random]

            print(sublist_sem3[sub_random3] + ' ' + class_lecture[lec_random] + ' ' + faculty_list[fac_random])
            db.session.commit()
