#!/usr/bin/env python
import time
import requests
try:
    from simplejson import json
except ImportError:
    import json

import uuid

def gen_uuid():
    return uuid.uuid4().hex

url = 'http://localhost:4000/reports/new'

values = {
    'report' : 'my_report',
    #'action' : {
    #    'smtp' : {
    #        'from' : 'stephane@wirtel.be',
    #        'to' : ['stephane@wirtel.be',],
    #        'subject' : 'Report',
    #    }
    #},
    #'action' : {
    #    'dropbox' : {
    #    }
    #},
    'data' : {
        'guid' : gen_uuid(),
        'name' : 'Stephane Wirtel',
        'date' : '15/09/1980',
        'time' : time.strftime('%Y-%m-%d %H:%M:%S'),
        'lines' : [
            {'firstname' : 'Stephane',
             'lastname' : 'Wirtel',
             'login' : 'stw',
            }
        ]
    }
}
jsonified = json.dumps(values)
headers = {'Content-Type' : 'application/json'}

query = requests.post(url, headers=headers, data=jsonified)
if query.ok:
    print json.loads(query.content)
