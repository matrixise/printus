#!/usr/bin/env python
from flask import Flask, g, session, jsonify
from flask import jsonify
from flask import request
from flask_rq import RQ
from flask.ext.babel import Babel, _

from printus.config import DefaultConfig
from printus.web.extensions import cache
from printus.web.extensions import db
from printus.web.extensions import login_manager
from printus.web.models import User

import printus.web.forms

# from werkzeug.local import LocalProxy
# from flask import _request_ctx_stack

# current_report = LocalProxy(lambda: _request_ctx_stack.top.report)

# def _report_context_processor():
#     return dict(current_user=_get_report())

# def _get_report():
#     return getattr(_request_ctx_stack.top, "report", None)

# def init_report(app):
#     app.context_processor(_report_context_processor)





__all__ = ['create_app']

class PrintUsApp(Flask):
    def __init__(self, *args, **kwargs):
        Flask.__init__(self, *args, **kwargs)

        self.config.from_object(DefaultConfig())

def configure_extensions(app):
    cache.init_app(app)

    babel = Babel(app)

    @babel.localeselector
    def locale_selector():
        return 'fr'

    # init_report(app)
    db.init_app(app)

    login_manager.login_view = 'general.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(long(user_id))

    login_manager.init_app(app)


def create_app(config=None):
    app = PrintUsApp(__name__)

    if config is not None:
        app.config.from_object(config)

    configure_extensions(app)

    import printus.web.views.general
    app.register_blueprint(printus.web.views.general.bp)

    # from rq_dashboard import RQDashboard
    # RQDashboard(app, url_prefix='/rq')


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
