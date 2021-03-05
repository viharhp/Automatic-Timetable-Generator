import random
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db, Subject


all_subject = Subject.query.order_by(Subject.id).all()
for subject in all_subject:
    if subject.sub_sem == 3:
        if subject.is_lab == 1:
            random = randint(10)
            print(random)
    else:
        print("Nope")
