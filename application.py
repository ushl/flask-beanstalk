#!/usr/bin/env python

from flask import Flask, request

application = Flask(__name__)

@application.route('/', methods=['GET'])
def hello():
    user = request.args.get('user')
    if not user:
        user = 'World'
    return "<p>Hello, %s!</p>\n" % user

if __name__ == "__main__":
    application.debug = True
    application.run()

