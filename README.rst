Django Singleton Model
======================

|Build Status|
==============

Singleton design-pattern implementation for using with django models and
works with more recent versions of django

Using
-----

Install the package

.. code:: bash

    $ pip3 install django-singleton-model

now you can import the SingletonModel class and inherit from it

.. code:: python

    from singleton_model import SingletonModel

    class MySingleModel(SingletonModel):
        pass

and that's it. Don't add it to INSTALLED\_APPS.

Running tests
-------------

Go into example folder

.. code:: bash

    $ cd example

and run them

.. code:: bash

    $ ./manage.py test

Troubleshooting
---------------

Check the example folder if you have any doubts. Or you can created an
issue it doesn't work anyway.

.. |Build Status| image:: https://travis-ci.org/icaropires/django-singleton-model.svg?branch=master
