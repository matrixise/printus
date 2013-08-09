How to Help
-----------

#. Check for open issues or open a fresh issue to start a discussion around a
   feature idea or a bug. There is a Contributor Friendly tag for issues that
   should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the
   **master** branch (or branch off of it).

#. Write a test which shows that the bug was fixed or that the feature works as
   expected.

#. Send a pull request and bug the maintainer until it gets merged and
   published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/matrixise/printus
.. _AUTHORS: https://github.com/matrixise/printus/blob/master/AUTHORS.rst


Runtime Environments
~~~~~~~~~~~~~~~~~~~~

PrintUs currently supports the following versions of Python:

- Python 2.6
- Python 2.7

Support for Python 3.x will do as soon as possible.

.. _virtualenv:

virtualenv
~~~~~~~~~~

Virtualenv is probably what you want to use during development, and if you have
shell access to your production machines, you will probably want to use it
there, too.

What problem does virtualenv solve? If you like Python as much as I do, chances
are you want to use it for other projects. But the more projects you have, the
more likely it is that you will be working with different versions of Python
itself, or at least different versions of Python libraries. Let's face it: quite
often libraries break backwards compatibility, and it's unlikely that any
serious application will have zero dependencies. So what do you do if two or
more of your projects have conflicting dependencies?

Virtualenv to the rescue! Virtualenv enables multiple side-by-side installations
of Python, one for each project. It does not actually install separate copies of
Python, but it does provide a clever way to keep different project environment
isolated. Let's see how virtualenv works.

If you are on Mac OSX or Linux, chances are that one of the following two
commands will work for you::

    $ sudo easy_install virtualenv

or even better::

    $ sudo pip install virtualenv

One of these will probably install virtualenv on your system. Maybe it's even in
your package manager. If you use Ubuntu, try::

    $ sudo apt-get install python-virtualenv

Once you have virtualenv installed, just fire up a shell and create your own
environment. I usually create a project folder and a `venv` folder within::

    $ virtualenv ~/.virtualens/venv
    New python executable in ~/.virtualenvs/venv/bin/python
    Installing distribute.............done.

Now, whenever you want to work on a project, you only have to active the
corresponding environment. On OS X and Linux, do the following::

    $ . ~/.virtualenvs/venv/bin/activate

Either way, you should now be using your virtualenv (notice how the prompt of
your shell has changed to show the active environment).

Now you can just enter the following command to get PrintUs activated in your
virtualenv::

    $ pip install PrintUs

A few seconds later and you are good to go.

Living on the Edge
~~~~~~~~~~~~~~~~~~

If you want to work with the latest version of PrintUs, there are two ways: you
can either let `pip` pull in the development version, or you can tell it to
operate on a git checkout. Either way, virtualenv is recommended.

Get the git checkout in a new virtualenv and run in development mode::

    $ git clone git://github.com/matrixise/printus.git
    $ cd printus
    $ virtualenv venv --distribute
    $ . venv/bin/activate
    $ python setup.py develop

This will pull in the dependencies and active the git head as the current
version inside the virtualenv. Then all you have to do is run ``git pull
origin`` to update to the latest version.

To just get the development version without git, do this instead::

    $ mkdir printus
    $ cd printus
    $ virtualenv venv --distribute
    $ pip install printus==dev


