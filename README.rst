A `Presenter First`_ implementation of a `Caesar Cipher`_ by `Sean Fisk`_ and `Gray Gwizdz`_.

.. _Caesar Cipher: http://en.wikipedia.org/wiki/Caesar_cipher
.. _Sean Fisk: mailto:sean@seanfisk.com
.. _Gray Gwizdz: mailto:gray.gwizdz@gmail.com
.. _Presenter First: http://atomicobject.com/pages/Presenter+First

.. image:: https://secure.travis-ci.org/seanfisk/caesar-cipher-presenter-first.png
   :target: https://secure.travis-ci.org/seanfisk/caesar-cipher-presenter-first

============
Installation
============

------------------------
Creating the environment
------------------------

Create a virtual python environment for the project.

For virtualenvwrapper add this to your ``.bashrc`` file in the user home directory::

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/project
    source /usr/local/bin/virtualenvwrapper.sh

If you're not using virtualenv or virtualenvwrapper you may skip this step.

For virtualenvwrapper (RECOMMENDED)::

    mkvirtualenv --no-site-packages caesar-cipher-presenter-first

For virtualenv::

    virtualenv --no-site-packages caesar-cipher-presenter-first
    source caesar-cipher-presenter-first-env/bin/activate

Clone the code::

    git clone https://github.com/seanfisk/caesar-cipher-presenter-first.git
    cd caesar-cipher-presenter-first

Install requirements. This only needs to be run once::

    pip install -r requirements/dev.txt

-----------
Running GUI
-----------

The Qt interface is written using PySide_ for Python bindings to the Qt_ library. Run the GUI in the following way using Shovel_::

    shovel qt

.. _PySide: http://qt-project.org/wiki/PySide
.. _Qt: http://qt-project.org/


---------------
Running the TUI
---------------

The text interface is written using Urwid_ for a curses-like interface on the command line. Run the TUI in the following way using Shovel_::

    shovel curses

.. _Urwid: http://excess.org/urwid/

-------------
Running tests
-------------

Test are written using ``unittest`` utilizing mocks created with ``mock``. Lint is run using flake8_. Run the tests in the following way using Shovel_::

    shovel test_all

.. _Shovel: https://github.com/seomoz/shovel
.. _flake8: https://pypi.python.org/pypi/flake8
