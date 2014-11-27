#!/usr/bin/python3

import bottle
import identigen

@bottle.route('/')
def route_root():
    return bottle.template('welcome_page')

@bottle.route('/', method='POST')
def route_paste_post():
    content = bottle.request.forms.get('content')
    return content + ' ' + identigen.generate(content)

@bottle.route('/<pid>')
@bottle.route('/<pid>/<pformat>')
def route_paste_get(pid, pformat='colored'):
    return 'paste: {}, {}'.format(pid, pformat)

if __name__ == '__main__':
    print('I: Starting application with development server')
    bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
else:
    print('I: Starting application as a wsgi application')
    application = bottle.default_app() # application used for wsgi mode
