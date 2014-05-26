#!/usr/bin/python2
from __future__ import print_function

import sys, os
import subprocess
from optparse import OptionParser

option_parser = OptionParser(usage='''
%prog [options] GRAPHITE_ROOT
''')
option_parser.add_option('--address', default='127.0.0.1', action='store', type=int, help='Interface to bind on (0.0.0.0 for all)')
option_parser.add_option('--port', default=8080, action='store', type=int, help='Port to listen on')
option_parser.add_option('--graphite-root', default='/usr/share/graphite-web', action='store', type=int, help='graphite static folder')

(options, args) = option_parser.parse_args()

django_admin = '/usr/bin/django-admin.py'
command = [
  django_admin,
  'runserver',
  '--pythonpath', python_path,
  '--settings', 'graphite.settings',  # will use the standard library settings and /etc/graphite/graphite_settings.py
  '{}:{}'.format(options.addres, options.port)
]

print('Running Graphite from {} under django development server'.format(options.graphite_root))
print(' '.join(command))
os.execvp(django_admin, command)
