Description
===========

WARNING: WIP !

A simple pastebin like service implemented in python3 with bottle.

The pastes storage backend are simple files.

It features the following:

- Syntaxic coloration (automatic detection) with `pygments`
- Simple and short urls (easy to copy by hands)
- Automatic purge of old pastes (1 month by default)
- Simple and nice theme.

It can be used directly (more for development) or from a wsgi compatible
web server.

Dependencies
============

- python3 (3.4 at least)
- bottle (included as submodule in this repository)
- pygments (packaged on a lot of distributions)

Installation
============

Dependencies:

.. code: shell

    # under deb based systems (debian/ubuntu for example)
    sudo apt-get install python3 python3-pygments

Clone this repository recursively:

.. code: shell

    git clone --recusive git://git.devys.org/pasteme
    cd pasteme
    # to run it with dev mode, just run it
    ./pastme.py

