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


Kubernetes
----------

Kubernetes support for foliolib can be activated by adding the following
section in the configuration file **server.conf** of the specific server
configuration directory:


.. code-block::

    [Kubernetes]
    enabled = True

So that the deployment works, Okapi needs to be running with
`service discovery enabled <https://github.com/folio-org/okapi/blob/master/doc/guide.md#kubernetes-integration>`_.

`Here <https://github.com/tobi-weber/foliolib/tree/master/extras/okapi-docker>`_ 
is a Dockerfile to build an image of Okapi with Kubernetes integration.
