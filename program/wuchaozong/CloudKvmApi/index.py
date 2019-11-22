#! /usr/bin/python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from service.image import Image
from service.instance import Instance
from service.disk import Disk
from service.network import Network
from service.monitor import Monitor
import json
import time
from service.instance import log
import traceback

def dispatch(**args):
    module = args["module"]
    func = args["action"]
    handler = None
    if module == "instance":
        handler = Instance()
    elif module == "disk":
        handler = Disk()
    elif module == "image":
        handler = Image()
    elif module == "network":
        handler = Network()
    elif module == "monitor":
        handler = Monitor()
    retv = getattr(handler, func)(**args)
    if "code" in retv:
        code = retv["code"]
        if code == 1:
            retv["code"] = 0
        elif code == 0:
            retv["code"] = 2
    return retv

def app(environ, start_response):

    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(request_body_size)
    request_body = json.loads(request_body)

    headers = [('Content-type', 'application/json')]
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    try:
        start = time.time()
        result = dispatch(**request_body)
        end = time.time()
        log("** %s Request:%s Response:%s **" %(now,request_body,json.dumps(result)))
        status = '200 OK'
        start_response(status, headers)
        return ['%s' % json.dumps(result)]
    except Exception as e:
        #log("** %s Request:%s Error:%s **" %(now,request_body,str(e)))
        log("** %s Request:%s Error:%s **" %(now,request_body,traceback.format_exc()))
        status = '500 Internal Server Error'
        start_response(status, headers)
        return ['%s' % str(e)]

httpd = make_server('', 9999, app)
print "listening port 9999 ..."
httpd.serve_forever()
