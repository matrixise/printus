# -*- coding: utf-8 -*-
import uuid
import datetime

from printus.web.extensions import db
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    name = db.Column(db.String(80))

    app_key = db.Column(db.String(80), unique=True)
    app_secret = db.Column(db.String(80))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('reports', lazy='dynamic'))

    uuid = db.Column(db.String(32), unique=True)

    created_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
    	super(Report, self).__init__(**kwargs)

    	self.uuid = uuid.uuid4().hex

    	self.created_at = datetime.datetime.now()

class ReportItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(32), unique=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))
    report = db.relationship('Report', backref=db.backref('items', lazy='dynamic'))
    
    created_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super(Feedback, self).__init__(**kwargs)

        self.created_at = datetime.datetime.now()

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('feedbacks', lazy='dynamic'))

    created_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super(Feedback, self).__init__(**kwargs)

        self.created_at = datetime.datetime.now()