import random
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db, Subject, Monday, Tuesday, Wednesday, Thursday, Friday

monday_subjects = Monday.query.order_by(Monday.m_id).all()
tuesday_subjects = Tuesday.query.order_by(Tuesday.t_id).all()
wednesday_subjects = Wednesday.query.order_by(Wednesday.w_id).all()
thursday_subjects = Thursday.query.order_by(Thursday.th_id).all()
friday_subjects = Friday.query.order_by(Friday.f_id).all()

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
                    monday_subject.asubject3 = subject.sub_name
                    credit = subject.sub_credits - 1
                    print(credit)
                    db.session.commit()
                elif monday_subject.bsubject3 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.bsubject3 = subject.sub_name
                    db.session.commit()
                elif monday_subject.csubject3 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.csubject3 = subject.sub_name
                    db.session.commit()
                else:
                    break
        elif subject.is_lab == 0:
            break
        else:
            break
    elif subject.sub_sem == 5:
        # verifying subject has lab or not
        if subject.is_lab == 1:
            # rnumber = random.randint(0,5)
            for monday_subject in monday_subjects:
                if monday_subject.asubject5 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.asubject5 = subject.sub_name
                    credit = subject.sub_credits - 1
                    print(credit)
                    db.session.commit()
                elif monday_subject.bsubject5 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.bsubject5 = subject.sub_name
                    db.session.commit()
                elif monday_subject.csubject5 == 'none':
                    print(" Added " + subject.sub_name)
                    monday_subject.csubject5 = subject.sub_name
                    db.session.commit()
                else:
                    break
        elif subject.is_lab == 0:
            break
        else:
            break
        elif subject.sub_sem == 7:
            # verifying subject has lab or not
            if subject.is_lab == 1:
                # rnumber = random.randint(0,5)
                for monday_subject in monday_subjects:
                    if monday_subject.asubject7 == 'none':
                        print(" Added " + subject.sub_name)
                        monday_subject.asubject7 = subject.sub_name
                        credit = subject.sub_credits - 1
                        print(credit)
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
            elif subject.is_lab == 0:
                break
            else:
                break
