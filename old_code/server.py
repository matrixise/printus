#!/usr/bin/env python
import uuid
import datetime
import logging
from pprint import pprint as pp
from functools import wraps


try:
    from simplejson import json
except ImportError:
    import json

from werkzeug.exceptions import HTTPException, NotFound, BadRequest
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from rq import Queue, Connection
from lib import generate_report
def gen_uuid():
    return uuid.uuid4().hex

def json_request(methods=None):
    def decorator(function):
        @wraps(function)
        def wrapper(self, request, *args, **kwargs):
            if 'json' in request.content_type:
                result = function(self, request, *args, **kwargs)
                if result is None:
                    result = {'status' : 'ok'}
                return Response(json.dumps(result))
            else:
                logging.getLogger('werkzeug').debug('Bad JSON Request')
                raise BadRequest()
        return wrapper
    return decorator

logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.DEBUG)

class PrintUsApp(object):
    def __init__(self, config):
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/reports/new', endpoint='reports_new'),
            Rule('/reports/get', endpoint='reports_get'),
        ])

        with Connection():
            self.queue = Queue()

        self.logger = logging.getLogger('report')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except NotFound, e:
            return self.error_404()
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def on_error404(self):
        return Response('This API does not exists', status=404)

    def on_index(self, request):
        now = datetime.datetime.now()
        return Response(now.strftime('%Y-%m-%d %H:%M:%S'))

    @json_request(methods=['POST'])
    def on_reports_new(self, request):
        info = json.loads(request.data)
        self.logger.debug('request: %r', info)
        info['uuid'] = gen_uuid()

        self.queue.enqueue(generate_report, info)

        values = {
            'status' : 'ok',
            'report_id' : info['uuid'],
        }
        return values

def create_application():
    config = None
    app = PrintUsApp(config)
    return app


if __name__ == '__main__':
    application = create_application()
    run_simple('localhost', 4000, application)
