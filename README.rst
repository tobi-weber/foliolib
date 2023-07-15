========
FolioLib
========

|PyPI| |Pythons| |ReadTheDocs|

.. |PyPI| image:: https://img.shields.io/pypi/v/foliolib.svg
   :alt: PyPI version
   :target: https://pypi.org/project/foliolib/

.. |Pythons| image:: https://img.shields.io/pypi/pyversions/foliolib.svg
   :alt: Supported Python versions
   :target: https://pypi.org/project/foliolib/

.. |ReadTheDocs| image:: https://readthedocs.org/projects/foliolib/badge/?version=latest
    :target: https://foliolib.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

FolioLib is an API-Client for `Folio <https://www.folio.org/>`_.
The API is generated from the RAML and OAS files from the Folio-Modules.

Documentation can be found at `https://foliolib.readthedocs.io/ <https://foliolib.readthedocs.io/>`_.

Python packages can be found at `https://pypi.org/project/foliolib/ <https://pypi.org/project/foliolib/>`_.

Debian packages can be found at `https://github.com/tobi-weber/foliolib/releases/latest/ <https://github.com/tobi-weber/foliolib/releases/latest/>`_.


Features:

- Python Folio API
- Commandline interface
- Install and manage Folio
- Install and manage Folio on Kubernetes
- Manage multiple Folio servers


Quickstart
==========

The installation requires python 3.6 or higher.

.. code-block:: bash

    pip install foliolib

Define a config for your Folio server:

.. code-block:: bash

    foliolib server create --help


.. code-block:: bash

    foliolib server create myServer -H okapi.server.url -p 9130

Make a Folio-API request:

.. code-block:: python

    >>> from foliolib import server
    >>> from foliolib.folio.users import Users
    >>> from foliolib.folio.api.inventory import Inventory
    >>>
    >>> server("myServer")
    >>>
    >>> Users("TenantId").login("UserId", "Password")
    >>> inventory = Inventory("TenantId")
    >>> instances = inventory.get_instances(query="title==*")
    >>> print(instances)

Also foliolib provides a command line interface:

.. code-block:: bash

    foliolib --help
