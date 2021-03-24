import random
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db, Subject, Monday, Tuesday, Wednesday, Thursday, Friday, Faculty, Classroom, Semester


def timetable():
    monday_subjects = Monday.query.order_by(Monday.m_id).all()
    tuesday_subjects = Tuesday.query.order_by(Tuesday.t_id).all()
    wednesday_subjects = Wednesday.query.order_by(Wednesday.w_id).all()
    thursday_subjects = Thursday.query.order_by(Thursday.th_id).all()
    friday_subjects = Friday.query.order_by(Friday.f_id).all()

    all_faculty = Faculty.query.order_by(Faculty.faculty_id).all()
    all_subjects = Subject.query.order_by(Subject.id).all()
    all_class = Classroom.query.order_by(Classroom.class_id).all()

    semester = Semester.query.get_or_404(1)    # gets 1st row of Semester table
    # subject list sem wise
    sublist_sem3a = []
    subcredits_sem3a = []
    sublab_sem3a = []
    sublist_sem3b = []
    subcredits_sem3b = []
    sublab_sem3b = []
    sublist_sem3c = []
    subcredits_sem3c = []
    sublab_sem3c = []

    sublist_sem5a = []
    subcredits_sem5a = []
    sublab_sem5a = []
    sublist_sem5b = []
    subcredits_sem5b = []
    sublab_sem5b = []
    sublist_sem5c = []
    subcredits_sem5c = []
    sublab_sem5c = []

    sublist_sem7a = []
    subcredits_sem7a = []
    sublab_sem7a = []
    sublist_sem7b = []
    subcredits_sem7b = []
    sublab_sem7b = []
    sublist_sem7c = []
    subcredits_sem7c = []
    sublab_sem7c = []

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
            sublist_sem3a.append(subject.sub_name)
            subcredits_sem3a.append(subject.sub_credits)
            sublab_sem3a.append(subject.is_lab)
            sublist_sem3b.append(subject.sub_name)
            subcredits_sem3b.append(subject.sub_credits)
            sublab_sem3b.append(subject.is_lab)
            sublist_sem3c.append(subject.sub_name)
            subcredits_sem3c.append(subject.sub_credits)
            sublab_sem3c.append(subject.is_lab)

        elif subject.sub_sem == 5:
            sublist_sem5a.append(subject.sub_name)
            subcredits_sem5a.append(subject.sub_credits)
            sublab_sem5a.append(subject.is_lab)
            sublist_sem5b.append(subject.sub_name)
            subcredits_sem5b.append(subject.sub_credits)
            sublab_sem5b.append(subject.is_lab)
            sublist_sem5c.append(subject.sub_name)
            subcredits_sem5c.append(subject.sub_credits)
            sublab_sem5c.append(subject.is_lab)
        elif subject.sub_sem == 7:
            sublist_sem7a.append(subject.sub_name)
            subcredits_sem7a.append(subject.sub_credits)
            sublab_sem7a.append(subject.is_lab)
            sublist_sem7b.append(subject.sub_name)
            subcredits_sem7b.append(subject.sub_credits)
            sublab_sem7b.append(subject.is_lab)
            sublist_sem7c.append(subject.sub_name)
            subcredits_sem7c.append(subject.sub_credits)
            sublab_sem7c.append(subject.is_lab)
        else:
            break

    for monday_subject in monday_subjects:
        sub_random3a = random.randint(0,len(sublist_sem3a)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        if monday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # Here we are first assigning subject, faculty and classroom randomly
            # After that we are removing faculty and classrom from list so that it can't get repeated in that row

            # subject assigning for Monday-3a
            monday_subject.asubject3 = sublist_sem3a[sub_random3a]
            monday_subject.aclass3 = class_lecture[lec_random]
            monday_subject.afaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random) # removing class
            faculty_list.pop(fac_random) # removing facult
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3a.pop(sub_random3a)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3b = random.randint(0,len(sublist_sem3b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3b
            monday_subject.bsubject3 = sublist_sem3b[sub_random3b]
            monday_subject.bclass3 = class_lecture[lec_random]
            monday_subject.bfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3b.pop(sub_random3b)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3c = random.randint(0,len(sublist_sem3c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3c
            monday_subject.csubject3 = sublist_sem3c[sub_random3c]
            monday_subject.cclass3 = class_lecture[lec_random]
            monday_subject.cfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3C
            #sublist_sem3c.pop(sub_random3c)
            db.session.commit()

            # -------------SEM-5------------------------

            # random selection of subject for sem5a
            sub_random5a = random.randint(0,len(sublist_sem5a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5a
            monday_subject.asubject5 = sublist_sem5a[sub_random5a]
            monday_subject.aclass5 = class_lecture[lec_random]
            monday_subject.afaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5a.pop(sub_random5a)
            db.session.commit()

            # random selection of subject for sem5b
            sub_random5b = random.randint(0,len(sublist_sem5b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5b
            monday_subject.bsubject5 = sublist_sem5b[sub_random5b]
            monday_subject.bclass5 = class_lecture[lec_random]
            monday_subject.bfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5b.pop(sub_random5b)
            db.session.commit()

            # random selection of subject for sem5c
            sub_random5c = random.randint(0,len(sublist_sem5c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5c
            monday_subject.csubject5 = sublist_sem5c[sub_random5c]
            monday_subject.cclass5 = class_lecture[lec_random]
            monday_subject.cfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5c.pop(sub_random5c)
            db.session.commit()

            # -------------SEM-7------------------------

            # random selection of subject for sem5a
            sub_random7a = random.randint(0,len(sublist_sem7a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7a
            monday_subject.asubject7 = sublist_sem7a[sub_random7a]
            monday_subject.aclass7 = class_lecture[lec_random]
            monday_subject.afaculty7 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7a.pop(sub_random7a)
            db.session.commit()

            # random selection of subject for sem7b
            sub_random7b = random.randint(0,len(sublist_sem7b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7b
            monday_subject.bsubject7 = sublist_sem7b[sub_random7b]
            monday_subject.bclass7 = class_lecture[lec_random]
            monday_subject.bfaculty7 = faculty_list[fac_random]

            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7b.pop(sub_random7b)
            db.session.commit()

            # random selection of subject for sem7c
            sub_random7c = random.randint(0,len(sublist_sem7c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7c
            monday_subject.csubject7 = sublist_sem7c[sub_random7c]
            monday_subject.cclass7 = class_lecture[lec_random]
            monday_subject.cfaculty7 = faculty_list[fac_random]

            #sublist_sem7c.pop(sub_random7c)
            db.session.commit()

            sublist_sem3a = []
            subcredits_sem3a = []
            sublab_sem3a = []
            sublist_sem3b = []
            subcredits_sem3b = []
            sublab_sem3b = []
            sublist_sem3c = []
            subcredits_sem3c = []
            sublab_sem3c = []

            sublist_sem5a = []
            subcredits_sem5a = []
            sublab_sem5a = []
            sublist_sem5b = []
            subcredits_sem5b = []
            sublab_sem5b = []
            sublist_sem5c = []
            subcredits_sem5c = []
            sublab_sem5c = []

            sublist_sem7a = []
            subcredits_sem7a = []
            sublab_sem7a = []
            sublist_sem7b = []
            subcredits_sem7b = []
            sublab_sem7b = []
            sublist_sem7c = []
            subcredits_sem7c = []
            sublab_sem7c = []

            for subject in all_subjects:
                if subject.sub_sem == 3:
                    sublist_sem3a.append(subject.sub_name)
                    subcredits_sem3a.append(subject.sub_credits)
                    sublab_sem3a.append(subject.is_lab)
                    sublist_sem3b.append(subject.sub_name)
                    subcredits_sem3b.append(subject.sub_credits)
                    sublab_sem3b.append(subject.is_lab)
                    sublist_sem3c.append(subject.sub_name)
                    subcredits_sem3c.append(subject.sub_credits)
                    sublab_sem3c.append(subject.is_lab)

                elif subject.sub_sem == 5:
                    sublist_sem5a.append(subject.sub_name)
                    subcredits_sem5a.append(subject.sub_credits)
                    sublab_sem5a.append(subject.is_lab)
                    sublist_sem5b.append(subject.sub_name)
                    subcredits_sem5b.append(subject.sub_credits)
                    sublab_sem5b.append(subject.is_lab)
                    sublist_sem5c.append(subject.sub_name)
                    subcredits_sem5c.append(subject.sub_credits)
                    sublab_sem5c.append(subject.is_lab)
                elif subject.sub_sem == 7:
                    sublist_sem7a.append(subject.sub_name)
                    subcredits_sem7a.append(subject.sub_credits)
                    sublab_sem7a.append(subject.is_lab)
                    sublist_sem7b.append(subject.sub_name)
                    subcredits_sem7b.append(subject.sub_credits)
                    sublab_sem7b.append(subject.is_lab)
                    sublist_sem7c.append(subject.sub_name)
                    subcredits_sem7c.append(subject.sub_credits)
                    sublab_sem7c.append(subject.is_lab)
                else:
                    break

            sublist_sem3a.pop(sub_random3a)
            sublist_sem3b.pop(sub_random3b)
            sublist_sem3c.pop(sub_random3c)
            sublist_sem5a.pop(sub_random5a)
            sublist_sem5b.pop(sub_random5b)
            sublist_sem5c.pop(sub_random5c)
            sublist_sem7a.pop(sub_random7a)
            sublist_sem7b.pop(sub_random7b)
            sublist_sem7c.pop(sub_random7c)

            faculty_list = []
            class_lab = []
            class_lecture = []

            for classes in all_class:
                if classes.class_type == 'lab':
                    class_lab.append(classes.class_number)
                elif classes.class_type == 'lecture':
                    class_lecture.append(classes.class_number)
                else:
                    break

            for faculty in all_faculty:
                faculty_list.append(faculty.faculty_name)
        else:
            break
    for tuesday_subject in tuesday_subjects:
        sub_random3a = random.randint(0,len(sublist_sem3a)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        if tuesday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # Here we are first assigning subject, faculty and classroom randomly
            # After that we are removing faculty and classrom from list so that it can't get repeated in that row

            # subject assigning for Monday-3a
            tuesday_subject.asubject3 = sublist_sem3a[sub_random3a]
            tuesday_subject.aclass3 = class_lecture[lec_random]
            tuesday_subject.afaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random) # removing class
            faculty_list.pop(fac_random) # removing facult
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3a.pop(sub_random3a)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3b = random.randint(0,len(sublist_sem3b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3b
            tuesday_subject.bsubject3 = sublist_sem3b[sub_random3b]
            tuesday_subject.bclass3 = class_lecture[lec_random]
            tuesday_subject.bfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3b.pop(sub_random3b)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3c = random.randint(0,len(sublist_sem3c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3c
            tuesday_subject.csubject3 = sublist_sem3c[sub_random3c]
            tuesday_subject.cclass3 = class_lecture[lec_random]
            tuesday_subject.cfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3C
            #sublist_sem3c.pop(sub_random3c)
            db.session.commit()

            # -------------SEM-5------------------------

            # random selection of subject for sem5a
            sub_random5a = random.randint(0,len(sublist_sem5a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5a
            tuesday_subject.asubject5 = sublist_sem5a[sub_random5a]
            tuesday_subject.aclass5 = class_lecture[lec_random]
            tuesday_subject.afaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5a.pop(sub_random5a)
            db.session.commit()

            # random selection of subject for sem5b
            sub_random5b = random.randint(0,len(sublist_sem5b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5b
            tuesday_subject.bsubject5 = sublist_sem5b[sub_random5b]
            tuesday_subject.bclass5 = class_lecture[lec_random]
            tuesday_subject.bfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5b.pop(sub_random5b)
            db.session.commit()

            # random selection of subject for sem5c
            sub_random5c = random.randint(0,len(sublist_sem5c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5c
            tuesday_subject.csubject5 = sublist_sem5c[sub_random5c]
            tuesday_subject.cclass5 = class_lecture[lec_random]
            tuesday_subject.cfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5c.pop(sub_random5c)
            db.session.commit()

            # -------------SEM-7------------------------

            # random selection of subject for sem5a
            sub_random7a = random.randint(0,len(sublist_sem7a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7a
            tuesday_subject.asubject7 = sublist_sem7a[sub_random7a]
            tuesday_subject.aclass7 = class_lecture[lec_random]
            tuesday_subject.afaculty7 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7a.pop(sub_random7a)
            db.session.commit()

            # random selection of subject for sem7b
            sub_random7b = random.randint(0,len(sublist_sem7b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7b
            tuesday_subject.bsubject7 = sublist_sem7b[sub_random7b]
            tuesday_subject.bclass7 = class_lecture[lec_random]
            tuesday_subject.bfaculty7 = faculty_list[fac_random]

            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7b.pop(sub_random7b)
            db.session.commit()

            # random selection of subject for sem7c
            sub_random7c = random.randint(0,len(sublist_sem7c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7c
            tuesday_subject.csubject7 = sublist_sem7c[sub_random7c]
            tuesday_subject.cclass7 = class_lecture[lec_random]
            tuesday_subject.cfaculty7 = faculty_list[fac_random]

            #sublist_sem7c.pop(sub_random7c)
            db.session.commit()

            sublist_sem3a = []
            subcredits_sem3a = []
            sublab_sem3a = []
            sublist_sem3b = []
            subcredits_sem3b = []
            sublab_sem3b = []
            sublist_sem3c = []
            subcredits_sem3c = []
            sublab_sem3c = []

            sublist_sem5a = []
            subcredits_sem5a = []
            sublab_sem5a = []
            sublist_sem5b = []
            subcredits_sem5b = []
            sublab_sem5b = []
            sublist_sem5c = []
            subcredits_sem5c = []
            sublab_sem5c = []

            sublist_sem7a = []
            subcredits_sem7a = []
            sublab_sem7a = []
            sublist_sem7b = []
            subcredits_sem7b = []
            sublab_sem7b = []
            sublist_sem7c = []
            subcredits_sem7c = []
            sublab_sem7c = []

            for subject in all_subjects:
                if subject.sub_sem == 3:
                    sublist_sem3a.append(subject.sub_name)
                    subcredits_sem3a.append(subject.sub_credits)
                    sublab_sem3a.append(subject.is_lab)
                    sublist_sem3b.append(subject.sub_name)
                    subcredits_sem3b.append(subject.sub_credits)
                    sublab_sem3b.append(subject.is_lab)
                    sublist_sem3c.append(subject.sub_name)
                    subcredits_sem3c.append(subject.sub_credits)
                    sublab_sem3c.append(subject.is_lab)

                elif subject.sub_sem == 5:
                    sublist_sem5a.append(subject.sub_name)
                    subcredits_sem5a.append(subject.sub_credits)
                    sublab_sem5a.append(subject.is_lab)
                    sublist_sem5b.append(subject.sub_name)
                    subcredits_sem5b.append(subject.sub_credits)
                    sublab_sem5b.append(subject.is_lab)
                    sublist_sem5c.append(subject.sub_name)
                    subcredits_sem5c.append(subject.sub_credits)
                    sublab_sem5c.append(subject.is_lab)
                elif subject.sub_sem == 7:
                    sublist_sem7a.append(subject.sub_name)
                    subcredits_sem7a.append(subject.sub_credits)
                    sublab_sem7a.append(subject.is_lab)
                    sublist_sem7b.append(subject.sub_name)
                    subcredits_sem7b.append(subject.sub_credits)
                    sublab_sem7b.append(subject.is_lab)
                    sublist_sem7c.append(subject.sub_name)
                    subcredits_sem7c.append(subject.sub_credits)
                    sublab_sem7c.append(subject.is_lab)
                else:
                    break

            sublist_sem3a.pop(sub_random3a)
            sublist_sem3b.pop(sub_random3b)
            sublist_sem3c.pop(sub_random3c)
            sublist_sem5a.pop(sub_random5a)
            sublist_sem5b.pop(sub_random5b)
            sublist_sem5c.pop(sub_random5c)
            sublist_sem7a.pop(sub_random7a)
            sublist_sem7b.pop(sub_random7b)
            sublist_sem7c.pop(sub_random7c)

            faculty_list = []
            class_lab = []
            class_lecture = []

            for classes in all_class:
                if classes.class_type == 'lab':
                    class_lab.append(classes.class_number)
                elif classes.class_type == 'lecture':
                    class_lecture.append(classes.class_number)
                else:
                    break

            for faculty in all_faculty:
                faculty_list.append(faculty.faculty_name)
        else:
            break
#--------------------Wednesday----------------------------
    for wednesday_subject in wednesday_subjects:
        sub_random3a = random.randint(0,len(sublist_sem3a)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        if wednesday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # Here we are first assigning subject, faculty and classroom randomly
            # After that we are removing faculty and classrom from list so that it can't get repeated in that row

            # subject assigning for Monday-3a
            wednesday_subject.asubject3 = sublist_sem3a[sub_random3a]
            wednesday_subject.aclass3 = class_lecture[lec_random]
            wednesday_subject.afaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random) # removing class
            faculty_list.pop(fac_random) # removing facult
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3a.pop(sub_random3a)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3b = random.randint(0,len(sublist_sem3b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3b
            wednesday_subject.bsubject3 = sublist_sem3b[sub_random3b]
            wednesday_subject.bclass3 = class_lecture[lec_random]
            wednesday_subject.bfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3b.pop(sub_random3b)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3c = random.randint(0,len(sublist_sem3c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3c
            wednesday_subject.csubject3 = sublist_sem3c[sub_random3c]
            wednesday_subject.cclass3 = class_lecture[lec_random]
            wednesday_subject.cfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3C
            #sublist_sem3c.pop(sub_random3c)
            db.session.commit()

            # -------------SEM-5------------------------

            # random selection of subject for sem5a
            sub_random5a = random.randint(0,len(sublist_sem5a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5a
            wednesday_subject.asubject5 = sublist_sem5a[sub_random5a]
            wednesday_subject.aclass5 = class_lecture[lec_random]
            wednesday_subject.afaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5a.pop(sub_random5a)
            db.session.commit()

            # random selection of subject for sem5b
            sub_random5b = random.randint(0,len(sublist_sem5b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5b
            wednesday_subject.bsubject5 = sublist_sem5b[sub_random5b]
            wednesday_subject.bclass5 = class_lecture[lec_random]
            wednesday_subject.bfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5b.pop(sub_random5b)
            db.session.commit()

            # random selection of subject for sem5c
            sub_random5c = random.randint(0,len(sublist_sem5c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5c
            wednesday_subject.csubject5 = sublist_sem5c[sub_random5c]
            wednesday_subject.cclass5 = class_lecture[lec_random]
            wednesday_subject.cfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5c.pop(sub_random5c)
            db.session.commit()

            # -------------SEM-7------------------------

            # random selection of subject for sem5a
            sub_random7a = random.randint(0,len(sublist_sem7a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7a
            wednesday_subject.asubject7 = sublist_sem7a[sub_random7a]
            wednesday_subject.aclass7 = class_lecture[lec_random]
            wednesday_subject.afaculty7 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7a.pop(sub_random7a)
            db.session.commit()

            # random selection of subject for sem7b
            sub_random7b = random.randint(0,len(sublist_sem7b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7b
            wednesday_subject.bsubject7 = sublist_sem7b[sub_random7b]
            wednesday_subject.bclass7 = class_lecture[lec_random]
            wednesday_subject.bfaculty7 = faculty_list[fac_random]

            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7b.pop(sub_random7b)
            db.session.commit()

            # random selection of subject for sem7c
            sub_random7c = random.randint(0,len(sublist_sem7c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7c
            wednesday_subject.csubject7 = sublist_sem7c[sub_random7c]
            wednesday_subject.cclass7 = class_lecture[lec_random]
            wednesday_subject.cfaculty7 = faculty_list[fac_random]

            #sublist_sem7c.pop(sub_random7c)
            db.session.commit()

            sublist_sem3a = []
            subcredits_sem3a = []
            sublab_sem3a = []
            sublist_sem3b = []
            subcredits_sem3b = []
            sublab_sem3b = []
            sublist_sem3c = []
            subcredits_sem3c = []
            sublab_sem3c = []

            sublist_sem5a = []
            subcredits_sem5a = []
            sublab_sem5a = []
            sublist_sem5b = []
            subcredits_sem5b = []
            sublab_sem5b = []
            sublist_sem5c = []
            subcredits_sem5c = []
            sublab_sem5c = []

            sublist_sem7a = []
            subcredits_sem7a = []
            sublab_sem7a = []
            sublist_sem7b = []
            subcredits_sem7b = []
            sublab_sem7b = []
            sublist_sem7c = []
            subcredits_sem7c = []
            sublab_sem7c = []

            for subject in all_subjects:
                if subject.sub_sem == 3:
                    sublist_sem3a.append(subject.sub_name)
                    subcredits_sem3a.append(subject.sub_credits)
                    sublab_sem3a.append(subject.is_lab)
                    sublist_sem3b.append(subject.sub_name)
                    subcredits_sem3b.append(subject.sub_credits)
                    sublab_sem3b.append(subject.is_lab)
                    sublist_sem3c.append(subject.sub_name)
                    subcredits_sem3c.append(subject.sub_credits)
                    sublab_sem3c.append(subject.is_lab)

                elif subject.sub_sem == 5:
                    sublist_sem5a.append(subject.sub_name)
                    subcredits_sem5a.append(subject.sub_credits)
                    sublab_sem5a.append(subject.is_lab)
                    sublist_sem5b.append(subject.sub_name)
                    subcredits_sem5b.append(subject.sub_credits)
                    sublab_sem5b.append(subject.is_lab)
                    sublist_sem5c.append(subject.sub_name)
                    subcredits_sem5c.append(subject.sub_credits)
                    sublab_sem5c.append(subject.is_lab)
                elif subject.sub_sem == 7:
                    sublist_sem7a.append(subject.sub_name)
                    subcredits_sem7a.append(subject.sub_credits)
                    sublab_sem7a.append(subject.is_lab)
                    sublist_sem7b.append(subject.sub_name)
                    subcredits_sem7b.append(subject.sub_credits)
                    sublab_sem7b.append(subject.is_lab)
                    sublist_sem7c.append(subject.sub_name)
                    subcredits_sem7c.append(subject.sub_credits)
                    sublab_sem7c.append(subject.is_lab)
                else:
                    break

            sublist_sem3a.pop(sub_random3a)
            sublist_sem3b.pop(sub_random3b)
            sublist_sem3c.pop(sub_random3c)
            sublist_sem5a.pop(sub_random5a)
            sublist_sem5b.pop(sub_random5b)
            sublist_sem5c.pop(sub_random5c)
            sublist_sem7a.pop(sub_random7a)
            sublist_sem7b.pop(sub_random7b)
            sublist_sem7c.pop(sub_random7c)

            faculty_list = []
            class_lab = []
            class_lecture = []

            for classes in all_class:
                if classes.class_type == 'lab':
                    class_lab.append(classes.class_number)
                elif classes.class_type == 'lecture':
                    class_lecture.append(classes.class_number)
                else:
                    break

            for faculty in all_faculty:
                faculty_list.append(faculty.faculty_name)
        else:
            break
# -----------------Thursday---------------

    for thursday_subject in thursday_subjects:
        sub_random3a = random.randint(0,len(sublist_sem3a)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        if thursday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # Here we are first assigning subject, faculty and classroom randomly
            # After that we are removing faculty and classrom from list so that it can't get repeated in that row

            # subject assigning for Monday-3a
            thursday_subject.asubject3 = sublist_sem3a[sub_random3a]
            thursday_subject.aclass3 = class_lecture[lec_random]
            thursday_subject.afaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random) # removing class
            faculty_list.pop(fac_random) # removing facult
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3a.pop(sub_random3a)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3b = random.randint(0,len(sublist_sem3b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3b
            thursday_subject.bsubject3 = sublist_sem3b[sub_random3b]
            thursday_subject.bclass3 = class_lecture[lec_random]
            thursday_subject.bfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3b.pop(sub_random3b)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3c = random.randint(0,len(sublist_sem3c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3c
            thursday_subject.csubject3 = sublist_sem3c[sub_random3c]
            thursday_subject.cclass3 = class_lecture[lec_random]
            thursday_subject.cfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3C
            #sublist_sem3c.pop(sub_random3c)
            db.session.commit()

            # -------------SEM-5------------------------

            # random selection of subject for sem5a
            sub_random5a = random.randint(0,len(sublist_sem5a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5a
            thursday_subject.asubject5 = sublist_sem5a[sub_random5a]
            thursday_subject.aclass5 = class_lecture[lec_random]
            thursday_subject.afaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5a.pop(sub_random5a)
            db.session.commit()

            # random selection of subject for sem5b
            sub_random5b = random.randint(0,len(sublist_sem5b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5b
            thursday_subject.bsubject5 = sublist_sem5b[sub_random5b]
            thursday_subject.bclass5 = class_lecture[lec_random]
            thursday_subject.bfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5b.pop(sub_random5b)
            db.session.commit()

            # random selection of subject for sem5c
            sub_random5c = random.randint(0,len(sublist_sem5c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5c
            thursday_subject.csubject5 = sublist_sem5c[sub_random5c]
            thursday_subject.cclass5 = class_lecture[lec_random]
            thursday_subject.cfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5c.pop(sub_random5c)
            db.session.commit()

            # -------------SEM-7------------------------

            # random selection of subject for sem5a
            sub_random7a = random.randint(0,len(sublist_sem7a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7a
            thursday_subject.asubject7 = sublist_sem7a[sub_random7a]
            thursday_subject.aclass7 = class_lecture[lec_random]
            thursday_subject.afaculty7 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7a.pop(sub_random7a)
            db.session.commit()

            # random selection of subject for sem7b
            sub_random7b = random.randint(0,len(sublist_sem7b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7b
            thursday_subject.bsubject7 = sublist_sem7b[sub_random7b]
            thursday_subject.bclass7 = class_lecture[lec_random]
            thursday_subject.bfaculty7 = faculty_list[fac_random]

            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7b.pop(sub_random7b)
            db.session.commit()

            # random selection of subject for sem7c
            sub_random7c = random.randint(0,len(sublist_sem7c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7c
            thursday_subject.csubject7 = sublist_sem7c[sub_random7c]
            thursday_subject.cclass7 = class_lecture[lec_random]
            thursday_subject.cfaculty7 = faculty_list[fac_random]

            #sublist_sem7c.pop(sub_random7c)
            db.session.commit()

            sublist_sem3a = []
            subcredits_sem3a = []
            sublab_sem3a = []
            sublist_sem3b = []
            subcredits_sem3b = []
            sublab_sem3b = []
            sublist_sem3c = []
            subcredits_sem3c = []
            sublab_sem3c = []

            sublist_sem5a = []
            subcredits_sem5a = []
            sublab_sem5a = []
            sublist_sem5b = []
            subcredits_sem5b = []
            sublab_sem5b = []
            sublist_sem5c = []
            subcredits_sem5c = []
            sublab_sem5c = []

            sublist_sem7a = []
            subcredits_sem7a = []
            sublab_sem7a = []
            sublist_sem7b = []
            subcredits_sem7b = []
            sublab_sem7b = []
            sublist_sem7c = []
            subcredits_sem7c = []
            sublab_sem7c = []

            for subject in all_subjects:
                if subject.sub_sem == 3:
                    sublist_sem3a.append(subject.sub_name)
                    subcredits_sem3a.append(subject.sub_credits)
                    sublab_sem3a.append(subject.is_lab)
                    sublist_sem3b.append(subject.sub_name)
                    subcredits_sem3b.append(subject.sub_credits)
                    sublab_sem3b.append(subject.is_lab)
                    sublist_sem3c.append(subject.sub_name)
                    subcredits_sem3c.append(subject.sub_credits)
                    sublab_sem3c.append(subject.is_lab)

                elif subject.sub_sem == 5:
                    sublist_sem5a.append(subject.sub_name)
                    subcredits_sem5a.append(subject.sub_credits)
                    sublab_sem5a.append(subject.is_lab)
                    sublist_sem5b.append(subject.sub_name)
                    subcredits_sem5b.append(subject.sub_credits)
                    sublab_sem5b.append(subject.is_lab)
                    sublist_sem5c.append(subject.sub_name)
                    subcredits_sem5c.append(subject.sub_credits)
                    sublab_sem5c.append(subject.is_lab)
                elif subject.sub_sem == 7:
                    sublist_sem7a.append(subject.sub_name)
                    subcredits_sem7a.append(subject.sub_credits)
                    sublab_sem7a.append(subject.is_lab)
                    sublist_sem7b.append(subject.sub_name)
                    subcredits_sem7b.append(subject.sub_credits)
                    sublab_sem7b.append(subject.is_lab)
                    sublist_sem7c.append(subject.sub_name)
                    subcredits_sem7c.append(subject.sub_credits)
                    sublab_sem7c.append(subject.is_lab)
                else:
                    break

            sublist_sem3a.pop(sub_random3a)
            sublist_sem3b.pop(sub_random3b)
            sublist_sem3c.pop(sub_random3c)
            sublist_sem5a.pop(sub_random5a)
            sublist_sem5b.pop(sub_random5b)
            sublist_sem5c.pop(sub_random5c)
            sublist_sem7a.pop(sub_random7a)
            sublist_sem7b.pop(sub_random7b)
            sublist_sem7c.pop(sub_random7c)

            faculty_list = []
            class_lab = []
            class_lecture = []

            for classes in all_class:
                if classes.class_type == 'lab':
                    class_lab.append(classes.class_number)
                elif classes.class_type == 'lecture':
                    class_lecture.append(classes.class_number)
                else:
                    break

            for faculty in all_faculty:
                faculty_list.append(faculty.faculty_name)
        else:
            break
# -------------Friday-----------------
    for friday_subject in friday_subjects:
        sub_random3a = random.randint(0,len(sublist_sem3a)-1) # length starts from 1 but list starts from 0 thus minus 1
        lab_random = random.randint(0,len(class_lab)-1)
        lec_random = random.randint(0,len(class_lecture)-1)
        fac_random = random.randint(0,len(faculty_list)-1)
        if friday_subject.asubject3 == 'none':
            # ----------------------SEM - 3 ---------------------
            # Here we are first assigning subject, faculty and classroom randomly
            # After that we are removing faculty and classrom from list so that it can't get repeated in that row

            # subject assigning for Monday-3a
            friday_subject.asubject3 = sublist_sem3a[sub_random3a]
            friday_subject.aclass3 = class_lecture[lec_random]
            friday_subject.afaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random) # removing class
            faculty_list.pop(fac_random) # removing facult
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3a.pop(sub_random3a)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3b = random.randint(0,len(sublist_sem3b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3b
            friday_subject.bsubject3 = sublist_sem3b[sub_random3b]
            friday_subject.bclass3 = class_lecture[lec_random]
            friday_subject.bfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3B
            #sublist_sem3b.pop(sub_random3b)
            db.session.commit()

            # Random values which doesn't include faculty and classroom assigned above.
            sub_random3c = random.randint(0,len(sublist_sem3c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-3c
            friday_subject.csubject3 = sublist_sem3c[sub_random3c]
            friday_subject.cclass3 = class_lecture[lec_random]
            friday_subject.cfaculty3 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #removing subject so that it can't get repeated again in further rows - FOR 3C
            #sublist_sem3c.pop(sub_random3c)
            db.session.commit()

            # -------------SEM-5------------------------

            # random selection of subject for sem5a
            sub_random5a = random.randint(0,len(sublist_sem5a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5a
            friday_subject.asubject5 = sublist_sem5a[sub_random5a]
            friday_subject.aclass5 = class_lecture[lec_random]
            friday_subject.afaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5a.pop(sub_random5a)
            db.session.commit()

            # random selection of subject for sem5b
            sub_random5b = random.randint(0,len(sublist_sem5b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5b
            friday_subject.bsubject5 = sublist_sem5b[sub_random5b]
            friday_subject.bclass5 = class_lecture[lec_random]
            friday_subject.bfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5b.pop(sub_random5b)
            db.session.commit()

            # random selection of subject for sem5c
            sub_random5c = random.randint(0,len(sublist_sem5c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-5c
            friday_subject.csubject5 = sublist_sem5c[sub_random5c]
            friday_subject.cclass5 = class_lecture[lec_random]
            friday_subject.cfaculty5 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem5c.pop(sub_random5c)
            db.session.commit()

            # -------------SEM-7------------------------

            # random selection of subject for sem5a
            sub_random7a = random.randint(0,len(sublist_sem7a)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7a
            friday_subject.asubject7 = sublist_sem7a[sub_random7a]
            friday_subject.aclass7 = class_lecture[lec_random]
            friday_subject.afaculty7 = faculty_list[fac_random]
            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7a.pop(sub_random7a)
            db.session.commit()

            # random selection of subject for sem7b
            sub_random7b = random.randint(0,len(sublist_sem7b)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7b
            friday_subject.bsubject7 = sublist_sem7b[sub_random7b]
            friday_subject.bclass7 = class_lecture[lec_random]
            friday_subject.bfaculty7 = faculty_list[fac_random]

            class_lecture.pop(lec_random)
            faculty_list.pop(fac_random)
            #sublist_sem7b.pop(sub_random7b)
            db.session.commit()

            # random selection of subject for sem7c
            sub_random7c = random.randint(0,len(sublist_sem7c)-1) # length starts from 1 but list starts from 0 thus minus 1
            lec_random = random.randint(0,len(class_lecture)-1)
            fac_random = random.randint(0,len(faculty_list)-1)

            # subject assigning for Monday-7c
            friday_subject.csubject7 = sublist_sem7c[sub_random7c]
            friday_subject.cclass7 = class_lecture[lec_random]
            friday_subject.cfaculty7 = faculty_list[fac_random]

            #sublist_sem7c.pop(sub_random7c)
            db.session.commit()

            sublist_sem3a = []
            subcredits_sem3a = []
            sublab_sem3a = []
            sublist_sem3b = []
            subcredits_sem3b = []
            sublab_sem3b = []
            sublist_sem3c = []
            subcredits_sem3c = []
            sublab_sem3c = []

            sublist_sem5a = []
            subcredits_sem5a = []
            sublab_sem5a = []
            sublist_sem5b = []
            subcredits_sem5b = []
            sublab_sem5b = []
            sublist_sem5c = []
            subcredits_sem5c = []
            sublab_sem5c = []

            sublist_sem7a = []
            subcredits_sem7a = []
            sublab_sem7a = []
            sublist_sem7b = []
            subcredits_sem7b = []
            sublab_sem7b = []
            sublist_sem7c = []
            subcredits_sem7c = []
            sublab_sem7c = []

            for subject in all_subjects:
                if subject.sub_sem == 3:
                    sublist_sem3a.append(subject.sub_name)
                    subcredits_sem3a.append(subject.sub_credits)
                    sublab_sem3a.append(subject.is_lab)
                    sublist_sem3b.append(subject.sub_name)
                    subcredits_sem3b.append(subject.sub_credits)
                    sublab_sem3b.append(subject.is_lab)
                    sublist_sem3c.append(subject.sub_name)
                    subcredits_sem3c.append(subject.sub_credits)
                    sublab_sem3c.append(subject.is_lab)

                elif subject.sub_sem == 5:
                    sublist_sem5a.append(subject.sub_name)
                    subcredits_sem5a.append(subject.sub_credits)
                    sublab_sem5a.append(subject.is_lab)
                    sublist_sem5b.append(subject.sub_name)
                    subcredits_sem5b.append(subject.sub_credits)
                    sublab_sem5b.append(subject.is_lab)
                    sublist_sem5c.append(subject.sub_name)
                    subcredits_sem5c.append(subject.sub_credits)
                    sublab_sem5c.append(subject.is_lab)
                elif subject.sub_sem == 7:
                    sublist_sem7a.append(subject.sub_name)
                    subcredits_sem7a.append(subject.sub_credits)
                    sublab_sem7a.append(subject.is_lab)
                    sublist_sem7b.append(subject.sub_name)
                    subcredits_sem7b.append(subject.sub_credits)
                    sublab_sem7b.append(subject.is_lab)
                    sublist_sem7c.append(subject.sub_name)
                    subcredits_sem7c.append(subject.sub_credits)
                    sublab_sem7c.append(subject.is_lab)
                else:
                    break

            sublist_sem3a.pop(sub_random3a)
            sublist_sem3b.pop(sub_random3b)
            sublist_sem3c.pop(sub_random3c)
            sublist_sem5a.pop(sub_random5a)
            sublist_sem5b.pop(sub_random5b)
            sublist_sem5c.pop(sub_random5c)
            sublist_sem7a.pop(sub_random7a)
            sublist_sem7b.pop(sub_random7b)
            sublist_sem7c.pop(sub_random7c)

            faculty_list = []
            class_lab = []
            class_lecture = []

            for classes in all_class:
                if classes.class_type == 'lab':
                    class_lab.append(classes.class_number)
                elif classes.class_type == 'lecture':
                    class_lecture.append(classes.class_number)
                else:
                    break

            for faculty in all_faculty:
                faculty_list.append(faculty.faculty_name)
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
'''
