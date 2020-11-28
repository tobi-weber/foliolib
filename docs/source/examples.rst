Example
=======


Install folio
-------------

Pyokapi provides an easy way to install Folio on your system.
As an example we use Folios `platform-core <https://github.com/folio-org/platform-core>`_.
This requires that Postgres, Docker, Okapi and Kafka are already installed and configured correctly.

First we need to run okapicli, to create the configuration directory.

.. code-block:: bash

    okapicli

Pyokapi provides the possibility to handle configurations for several servers.
For now we need to edit the default configuration under $HOME/.pyokapi/default/okapi.conf.
Set the correct values for the Okapi and Postgres installation:

.. code-block::

    [Okapi]
    host = 192.168.99.66
    port = 9130
    
    [Postgres]
    host = 192.168.99.66
    port = 5432
    user = postgres
    password = postgres


The configuration for the modules can be done in the directory $HOME/.pyokapi/default/modules.
Here we need to configure the module mod-pubsub for the kafka installation.
Edit the file $HOME/.pyokapi/default/modules/mod-pubsub.conf and set the values for your Kafka
installation and set the Okapi url:

.. code-block::

    [Env]
    KAFKA_HOST = 192.168.10.2
    KAFKA_PORT = 9092
    OKAPI_URL = http://192.168.10.2:9130


For the installation clone the platform-core repository:

.. code-block:: bash

    git clone https://github.com/folio-org/platform-core
    cd platform-core
    git checkout q3-2020


Assuming you have set a password for your postgres installation you can create
the databases for Okapi and Folio with okapicli:


.. code-block:: bash
    
    okapicli initdb -u okapi -p okapi25 -d okapi
    okapicli initmoduledb -u folio_admin -p folio_admin -d okapi_modules


Configure the Okapi enviroment with the database for module data:


.. code-block:: bash

    okapicli db -u folio_admin -p folio_admin -d okapi_modules

 
Next we need to create a tenant:

.. code-block:: bash
    
    okapicli addTenant mylib -a myLibrary -d 'My Library'


And now we can start the installation:

.. code-block:: bash

    okapicli installModules path/to/platform-core/okapi-install.json mylib --loadSample --loadReference
    foliocli installStripesModules path/to/platform-core/stripes-install.json mylib


Folio is now installed and we need a superuser to have access:

.. code-block:: bash

    foliocli superuser mylib -u folio_admin -u admin


Now you can start the webfrontend and login:

.. code-block:: bash
    
    cd platform-core
    yarn install
    yarn start











