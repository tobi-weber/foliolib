Documentation
=============

Configuration
-------------

The configuration files are kept in the **$HOME/.foliolib** folder by default.
The path for the configuration can be overridden with the **$FOLIOLIB_CONFDIR**
environment variable.

Each Folio server has specific configuration files within the configruation
path.
For example, the configuration for a server named **myFolio** is given the path
**$HOME/.foliolib/myFolio/**.

The configuration file **$HOME/.foliolib/foliolib.conf** contains general
parameters necessary for foliolib.

For a server configuration **myFolio** the configuration file
**$HOME/.foliolib/myFolio/server.conf** and a folder
for module specific configurations **$HOME/.foliolib/myFolio/modules**
are created .

A server configuration can be created from the command line:


.. code-block:: bash

    foliolib server create myFolio -H okapi.server.url


The modules directory contains configuration files for specific modules.
The name of the file is modulename.conf, e.g. mod-pubsub.conf.


Python Folio API
----------------

The `Python Folio API <https://foliolib.readthedocs.io/en/latest/foliolib.folio.api.html>`_
is generated from the RAML and OAS files from the Folio-Modules.

To call a function of the foliolib API, a server config must be loaded:

.. code-block:: python

    from foliolib import server
    server("SERVER_NAME")

and a authentication must be performed on the tenant(s),
which should be called:

.. code-block:: python

    from foliolib.folio.users import Users
    Users("TENANT_ID").login("USER_ID","PASSWORD")

Now Folio API functions can be called.
For example a query for `instances <https://foliolib.readthedocs.io/en/latest/generated/foliolib.folio.api.inventory.Inventory.html#foliolib.folio.api.inventory.Inventory.get_instances>`_
can be performed:

.. code-block:: python

    from foliolib.folio.api.inventory import Inventory
    inventory = Inventory("TENANT_ID")
    instances = inventory.get_instances(query="title==*")
    print(instances)

Here is an example to get all `deployed modules <https://foliolib.readthedocs.io/en/latest/generated/foliolib.okapi.okapiClient.OkapiClient.html#foliolib.okapi.okapiClient.OkapiClient.get_deployed_modules>`_.
If Okapi is secured, an authentication on the Supertenant is needed:

.. code-block:: python

    from foliolib import server
    from foliolib.folio.users import Users
    from foliolib.okapi.okapiClient import OkapiClient

    server("SERVER_NAME")

    Users("supertenant").login("USER_ID","PASSWORD")

    okapi = OkapiClient()
    modules = okapi.get_deployed_modules()
    print(modules)




Folio Enviroment Variables
--------------------------

By default foliolib manages the global variables for the Folio
modules itself. This can be changed via the **foliolibenv** configuration
parameter in the **Okapi** section of the **server.conf** configuration file.
If **foliolibenv** is set to **False**, the global parameters are
stored in Okapi, or if Kubernetes is used, stored in a Kubernetes-Secret
for all Folio modules.

If foliolib handles the module parameters, global parameters can be
overwritten with module specific parameters with a configuration file
inside the modules directory of the defined server.
Otherwise global parameters will overwrite module specific parameters.

Example for the **Env** section in the **server.conf** configuration file:


.. code-block:: cfg

    [Env]
    db_host = postgres
    db_port = 5432
    db_username = folio
    db_password = folio
    db_database = okapi_modules
    db_charset = UTF-8
    kafka_host = kafka
    kafka_port = 9092
    okapi_url = http://okapi:9130



Kubernetes
----------

Kubernetes support for foliolib can be activated by adding the following
section in the configuration file **server.conf** of the specific server
configuration directory:


.. code-block:: cfg

    [Kubernetes]
    enabled = True

In order to connect to Kubernetes, a Kubernetes config file its needed.
This can be a file **kube_config** inside the server config path
($HOME/.foliolib/[Server Name]/kube_config) or the path can be set in the
section **Kubernetes** with the key **kube_config** in the **server.conf**
configuration file.

By default foliolib expects that a namespace with the name **folio** exists.
The namespace can be set in the section **Kubernetes** with the key
**namespace** in  the **server.conf** configuration file.

So that the deployment works, Okapi needs to be running with
`service discovery enabled <https://github.com/folio-org/okapi/blob/master/doc/guide.md#kubernetes-integration>`_.

`Here <https://github.com/tobi-weber/foliolib/tree/master/extras/okapi-docker>`_
is a Dockerfile to build an image of Okapi with Kubernetes integration.


Module Configuration
--------------------


The **$HOME/.foliolib/[Server Name]/modules** directory contains configuration
files for modules.
The name of the file is **[Module Name].conf**, e.g. mod-search.conf.
Module configurations can be Enviroment variables and Kubernetes specific
parameters.

Example for the mod-search module **mod-search.conf**:

.. code-block:: cfg

    [Env]
    ELASTICSEARCH_URL = http://elasticsearch:9200
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_HOST = elasticsearch
    ELASTICSEARCH_USERNAME = elastic
    ELASTICSEARCH_PASSWORD = elastic
    INITIAL_LANGUAGES = eng,ger
    SYSTEM_USER_PASSWORD = mod-search-secret


Example for the **mod-erm-usage-harvester.conf** to enable Hazelcast
for Kubernetes:


.. code-block:: cfg

    [Kubernetes]
    hazelcast = True
