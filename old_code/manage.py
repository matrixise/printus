#!/usr/bin/env python

import os

from flask import current_app
from flask.ext.script import Manager
from printus.web import create_app
from printus.web.extensions import db
from printus.web.models import *

def main():
    manager = Manager(create_app)

    @manager.command
    def show_routes():
        print current_app.url_map

    @manager.command
    def db_populate():
        user_admin = User(name='Administrator', username='admin', password='admin', email='admin@printus.io')
        db.session.add(user_admin)

        for i in range(1, 100):
            report = Report(user=user_admin, name='My Report {}'.format(i))
            db.session.add(report)

        db.session.commit()


    @manager.command
    def db_create_all():
        db.create_all()

    @manager.command
    def db_drop_all():
    	db.drop_all()

    manager.run()

if __name__ == '__main__':
    main()
