# configuration file of pastme service

import os.path

# the directory where the pastes are stored
pastedir = '/pastes' if os.path.exists('/pastes') else '/tmp/pastes'

# how many days a paste remain stored
timeout = 30
