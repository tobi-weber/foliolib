Documentation
=============

Configuration
-------------

After the first run of okapicli a configuration with default values will be created
under $HOME/.foliolib.


``$HOME/.foliolib/foliolib.conf``
*********************************

.. code-block:: bash

    [PullNode]
    host = folio-registry.aws.indexdata.com
    port = 80
    
    [Cache]
    descriptors = /home/tobi/.foliolib/cache/descriptors

* PullNode
    * host: The hostname where to pull module descriptors
    * port: The port of the host
* Cache
    * descriptors: Directory where the pulled module descriptors are cached.


``$HOME/.foliolib/default``
***************************

The default directory contains configuration files for the default server config.
FolioLib provides the ability to have serveral server configs, which can be managed through the
okapicli tool.


``$HOME/.foliolib/default/okapi.conf``
**************************************

.. code-block::

    [Okapi]
    host = 192.168.99.66
    port = 9130
    
    [Postgres]
    host = 192.168.99.66
    port = 5432
    user = postgres
    password = postgres

* Okapi
    * host: The hostname of okapi 
    * port: The port of the okapi host
* Postgres
    * host: The hostname of the postgres server
    * port: The port of the postgres server
    * user: Administrator username of the postgres server
    * password: Administrator password of the postgres server

``$HOME/.foliolib/default/modules``
***********************************

The modules directory contains configuration files for specific modules.
The name of the file is modulename.conf, e.g. mod-pubsub.conf.
It is possible to define module properties, which will be added or modified in the module
descriptor, if a module will be added to Okapi.

Example ``$HOME/foliolib/default/modules/mod-users.conf``:

.. code-block::

    [Env]
    JAVA_OPTIONS = -XX:MaxRAMPercentage=66.0

    [Docker]
    Memory = 536870912

Example ``$HOME/foliolib/default/modules/mod-pubsub.conf``:

.. code-block::

    [Env]
    KAFKA_HOST = 192.168.10.2
    KAFKA_PORT = 9092
    OKAPI_URL = http://192.168.10.2:9130
    JAVA_OPTIONS = -XX:MaxRAMPercentage=66.0 -XX:+HeapDumpOnOutOfMemoryError

    [Docker]
    Memory = 1073741824


Command-line interfaces
-----------------------

The commadline interfaces ``okapicle`` and ``foliocli`` have several subcommads.


okapicli
********

.. code-block::

    $ okapicli --help
    usage: okapicli <command> [<args>]
    
       Commands:
    
        db                      Set db in env
        installModules          Add, deploy and enable modules for a tenant
        addModule               Add module by name and version
        addModules              Add modules descriptors from json dict
        addModuleDescriptor     Add a modul from Moduledescriptor.json
        addModuleDescriptors    Add modules descriptors from dir with ModuleDescriptor.json files
        removeModule            Remove a modul
        deployModule            Deploy a modul for a node
        undeployModule          Undeploy a modul
        enableModule            Enable a modul for a tenant
        enableModules           Enable a moduls for a tenant
        disableModule           Disable a modul
        addTenant               Create a tenant
        removeTenant            Remove a tenant
    
      Inspection
        version                 Show Okapi version
        health                  Show health of modules
        env                     Show env
        nodes                   Show nodes
        module                  Show ModulDescriptor of a module
        modules                 Show modules
        deployed                Show deployes modules
        tenants                 Show tenants
        tenantModules           Show mods of a tenant
        tenantInterface         Show interface for a tenant
        tenantInterfaces        Show interfaces for a tenant
    
      Database
        initdb                  Initialize okapi db
        initmoduledb            Initialize module db
    
      foliolib
        servers                 List available server configs
        setServer               Set server config
        createServer            Create new server config
        delServer               Delete a server config
    
    Okapi command line interface
    
    positional arguments:
      command     Subcommand to run
    
    optional arguments:
      -h, --help  show this help message and exit



foliocli
********

.. code-block::

    $ foliocli --help
    usage: foliocli <command> [<args>]
    
       Commands:
    
        installStripesModules   Add and enable stipes modules
        superuser               Create a superuser
        secureOkapi             Secure Okapi
        loginOkapi              Login Okapi
    
      foliolib
        servers                 List available server configs
        setServer               Set server config
        createServer            Create new server config
        delServer               Delete a server config
    
    Folio command line interface
    
    positional arguments:
      command     Subcommand to run
    
    optional arguments:
      -h, --help  show this help message and exit

    


Subcommands
***********

To show the help of a subcommand:

.. code-block:: bash
    
    okapicli installModules --help




