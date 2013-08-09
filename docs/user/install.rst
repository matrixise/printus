.. _install:

Installation
------------

This part of the documentation covers the installation of PrintUs.
The first step to using any software package is getting it properly installed.

PrintUs depends on a lot of external libraries. `Flask
<http://flask.pocoo.org/>`_ and `RQ <http://python-rq.org>`_.

Flask is a micro-framework for the web development, and RQ is Redis Queue
written in Python.

You will need Python 2.6 or higher to get started, so be sure to have an
up-to-date Python 2.x installation.

Distribute & Pip
~~~~~~~~~~~~~~~~

Installing printus is simple with `pip <http://www.pip-installer.org/>`_::

    $ pip install printus

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_::
    
    $ easy_install printus

But, you really `shouldn't do that <http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install>`_.

Cheeseshop Mirror
~~~~~~~~~~~~~~~~~

If the Cheeseshop is down, you can also install PrintUs from one of the mirrors.
`Crate.io <http://crate.io>`_ is one of them::

    $ pip install -i http://simple.crate.io/ printus

Get the code
~~~~~~~~~~~~

PrintUs is actively developed on GitHub, where the code is `always available
<https://github.com/matrixise/printus>`_.

You can either clone the public repository::

    $ git clone git://github.com/matrixise/printus.git

Download the `tarball <https://github.com/matrixise/printus/tarball/master>`_::

    $ curl -OL https://github.com/matrixise/printus/tarball/master

Or, download the `zipball <https://github.com/matrixise/printus/zipball/master>`_::
    
    $ curl -OL https://github.com/matrixise/printus/zipball/master


Once you have a copy of the source, you can embed it in your Python package, or
install it into your site-packages easily::

    $ python setup.py install

