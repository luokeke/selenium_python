#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 14:56
# @Author : liuhuiling
#  https://trypyramid.com/
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

# 访问地址 : http://127.0.0.1:6543/