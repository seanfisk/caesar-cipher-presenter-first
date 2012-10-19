A `Presenter First`_ implementation of Sean's previous `Caesar cipher program`_.

.. image:: https://secure.travis-ci.org/seanfisk/caesar-cipher-presenter-first.png
   :target: https://secure.travis-ci.org/seanfisk/caesar-cipher-presenter-first

.. _Presenter First: http://atomicobject.com/pages/Presenter+First
.. _Caesar cipher program: https://github.com/seanfisk/caesar-cipher

Test are written using ``unittest`` utilizing mocks created with ``mock``.

Shovel_ is used for running miscellaneous tasks. Run the tests in the following way::

    pip install -r requirements-test.txt # only needs to be run once
    shovel test

.. _Shovel: https://github.com/seomoz/shovel
