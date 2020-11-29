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

FolioLib is a manager and library for `Okapi <https://github.com/folio-org/okapi>`_ 
and `Folio <https://www.folio.org/>`_.
The Library is automatically generated from the RAML files of the different Folio-Modules.

Documentation can be found `here <https://foliolib.readthedocs.io/>`_.


Installation
============

The installation requires python 3.6 or higher.

.. code-block:: bash

    pip install foliolib


Command-line interfaces
#######################

FolioLib provides two command-line interfaces.

.. code-block:: bash

    okapicli --help

After the first call of okapicli, foliolib creates a directory with configurations
under $HOME/.foliolib.


.. code-block:: bash

    foliocli --help









