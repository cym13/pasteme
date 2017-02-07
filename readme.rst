Description
===========

A simple pastebin like service implemented in python3 with bottle. This is
a free software as defined by http://opensource.org/osd.

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

.. code:: shell

    # under deb based systems (debian/ubuntu for example)
    sudo apt-get install python3 python3-pygments

Clone this repository recursively:

.. code:: shell

    git clone --recursive git://git.devys.org/pasteme
    cd pasteme
    # to run it with dev mode, just run it
    ./pastme.py

License
=======

Unless specified otherwise, this project is licensed under the terms of the
GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. You
should have received a copy of the GNU General Public License along with this
program. If not, see <https://opensource.org/licenses/GPL-3.0> or
<http://www.gnu.org/licenses/>.

SPDX-License-Identifier: GPL-3.0+

Copyright © 2016 vg <vg@devys.org>

Credits
=======

The original git repository for this project can be found at
http://git.devys.org/pasteme/

The keyboard keys icons are from a set_ designed by Chromatix.
They are licensed as `CC Attribution-NonCommercial-No Derivate 4.0`__.

.. _set: http://www.iconarchive.com/show/keyboard-keys-icons-by-chromatix.2.html
.. __: http://creativecommons.org/licenses/by-nc-nd/4.0/legalcode

The pygments theme come from *Sourcey*: http://sourcey.com
