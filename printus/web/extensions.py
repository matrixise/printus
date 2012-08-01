# -*- coding: utf-8 -*-

from flask.ext.cache import Cache
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
#: A proxy for the current user.

__all__ = ['cache', 'db']

cache = Cache()

db = SQLAlchemy()

login_manager = LoginManager()