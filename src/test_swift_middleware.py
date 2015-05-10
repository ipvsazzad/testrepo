def app(environ, start_response):
    response_body = 'The WSGI request environment looks like this: %r' % environ
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response('200 OK', response_headers)
    return [response_body]


class TrivialMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        return self.app(environ, start_response)