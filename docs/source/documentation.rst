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

For a server configuration myFolio the configuration file
**$HOME/.foliolib/myFolio/server.conf** is created and a folder
for module specific configurations **$HOME/.foliolib/modules**.

A server configuration can be created from the command line:


.. code-block:: bash

    foliolib server create myFolio -H okapi.server.url


The modules directory contains configuration files for specific modules.
The name of the file is modulename.conf, e.g. mod-pubsub.conf.


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


.. code-block:: bash

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


.. code-block::

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

.. code-block::

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


.. code-block::

    [Kubernetes]
    hazelcast = True
