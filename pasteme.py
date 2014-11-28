#!/usr/bin/python3

import bottle
import identigen
import config
from pathlib import Path

pathbase = Path(config.pastedir)

if not pathbase.exists():
    pathbase.mkdir(mode=0o700, parents=True)

@bottle.route('/')
def route_root():
    return bottle.template('root')

@bottle.route('/', method='POST')
def route_paste_post():
    content = bottle.request.forms.get('content')
    pid = identigen.generate(content)
    path = pathbase / pid
    with path.open(mode='wb') as fd:
        fd.write(content.encode('utf8'))
    bottle.redirect('/' + pid)

@bottle.route('/<pid>')
@bottle.route('/<pid>/<pformat>')
def route_paste_get(pid, pformat='colored'):
    if pformat != 'colored' and pformat != 'raw':
        return bottle.template('bad_format')
    path = pathbase / pid
    try:
        with path.open() as fd:
            content = fd.read()
    except IOError:
        # use this template for all file based exception
        return bottle.template('not_found')
    return bottle.template('paste', content=content)

if __name__ == '__main__':
    print('I: Starting application with development server')
    bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
else:
    print('I: Starting application as a wsgi application')
    application = bottle.default_app() # application used for wsgi mode
